import time
from typing import List, Optional
from playwright.sync_api import sync_playwright, Page
from dataclasses import dataclass, asdict, field
import pandas as pd
import argparse
import os
import random

@dataclass
class Business:
    name: str = ""
    address: str = ""
    website: str = ""
    phone_number: str = ""
    google_maps_url: str = ""
    location_area: str = ""
    reviews_count: Optional[int] = None
    reviews_average: Optional[float] = None
    last_3_reviews: str = ""
    business_type: str = ""
    opening_hours: str = ""
    description: str = ""
    keyword: str = ""  # New field for search query
    rank: int = 0     # New field for ranking

def extract_text_safe(page: Page, xpath: str) -> str:
    try:
        if page.locator(xpath).count() > 0:
            return page.locator(xpath).first.inner_text()
    except:
        pass
    return ""

def extract_last_3_reviews(page: Page) -> str:
    reviews = []
    try:
        page.mouse.wheel(0, 1500)
        page.wait_for_timeout(2000)
        
        review_elements = page.locator('//div[contains(@class, "jftiEf")]').all()[:3]
        for i, review_element in enumerate(review_elements):
            try:
                review_text = review_element.locator('.//span[contains(@class, "wiI7pd")]').first.inner_text()
                if review_text and review_text.strip():
                    clean_review = review_text.replace('\n', ' ').strip()
                    reviews.append(f"Review {i+1}: {clean_review[:150]}{'...' if len(clean_review) > 150 else ''}")
            except:
                continue
                
        if not reviews:
            review_texts = page.locator('//span[contains(@class, "wiI7pd")]').all()[:3]
            for i, review_text in enumerate(review_texts):
                try:
                    text = review_text.inner_text()
                    if text and text.strip():
                        clean_text = text.replace('\n', ' ').strip()
                        reviews.append(f"Review {i+1}: {clean_text[:150]}{'...' if len(clean_text) > 150 else ''}")
                except:
                    continue
                    
    except:
        pass
    
    return " | ".join(reviews) if reviews else "No reviews found"

def extract_opening_hours(page: Page) -> str:
    try:
        hours_selectors = [
            '//div[contains(@class, "t39EBf")]',
            '//div[@class="OMl5r"]',
            '//div[contains(@class, "y0skZc")]',
            '//div[contains(@class, "WgFkxc")]',
            '//div[contains(@class, "mxowUb")]'
        ]
        
        for selector in hours_selectors:
            hours_text = extract_text_safe(page, selector)
            if hours_text and len(hours_text) > 10:
                return hours_text
        
        status = extract_text_safe(page, '//div[contains(@class, "o0Svhf")]')
        if status:
            return status
            
    except:
        pass
    
    return "Not available"

def extract_location_area(address: str) -> str:
    if not address:
        return ""
    
    area_indicators = [' near ', ' opposite ', ' beside ', ' next to ', ' behind ', ' in front of ']
    
    for indicator in area_indicators:
        if indicator in address.lower():
            parts = address.lower().split(indicator)
            if len(parts) > 1:
                area = parts[1].split(',')[0].strip()
                return area.title()
    
    parts = address.split(',')
    if len(parts) >= 2:
        return parts[-2].strip()
    
    return ""

def extract_business_details(page: Page) -> Business:
    business = Business()
    
    business.name = extract_text_safe(page, '//div[@class="TIHn2 "]//h1[@class="DUwDvf lfPIob"]')
    
    if not business.name:
        business.name = extract_text_safe(page, '//h1[contains(@class, "DUwDvf")]') or "Unknown Business"
    
    business.address = extract_text_safe(page, '//button[@data-item-id="address"]//div[contains(@class, "fontBodyMedium")]')
    business.website = extract_text_safe(page, '//a[@data-item-id="authority"]//div[contains(@class, "fontBodyMedium")]')
    business.phone_number = extract_text_safe(page, '//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]')
    business.business_type = extract_text_safe(page, '//div[@class="LBgpqf"]//button[@class="DkEaL "]')
    
    business.location_area = extract_location_area(business.address)
    
    reviews_count_raw = extract_text_safe(page, '//div[@class="TIHn2 "]//div[@class="fontBodyMedium dmRWX"]//div//span//span//span[@aria-label]')
    if reviews_count_raw:
        try:
            temp = reviews_count_raw.replace('\xa0', '').replace('(','').replace(')','').replace(',','')
            business.reviews_count = int(temp)
        except:
            pass
    
    reviews_avg_raw = extract_text_safe(page, '//div[@class="TIHn2 "]//div[@class="fontBodyMedium dmRWX"]//div//span[@aria-hidden]')
    if reviews_avg_raw:
        try:
            temp = reviews_avg_raw.replace(' ','').replace(',','.')
            business.reviews_average = float(temp)
        except:
            pass
    
    business.opening_hours = extract_opening_hours(page)
    
    business.description = extract_text_safe(page, '//div[@class="WeS02d fontBodyMedium"]//div[@class="PYvSYb "]') or "None Found"
    
    business.google_maps_url = page.url
    
    business.last_3_reviews = extract_last_3_reviews(page)
    
    return business

def wait_for_business_details(page: Page, timeout: int = 8000) -> bool:
    try:
        page.wait_for_selector('//div[@class="TIHn2 "]//h1[@class="DUwDvf lfPIob"]', timeout=timeout)
        return True
    except:
        try:
            page.wait_for_selector('//h1[contains(@class, "DUwDvf")]', timeout=3000)
            return True
        except:
            try:
                page.wait_for_selector('//button[@data-item-id="address"]', timeout=3000)
                return True
            except:
                if page.locator('//a[contains(@href, "https://www.google.com/maps/place")]').count() > 0:
                    return False
                return False

def scrape_businesses_with_scrolling(search_query: str, total: int) -> List[Business]:
    businesses: List[Business] = []
    seen_businesses = set()
    
    with sync_playwright() as p:
        browser_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        browser = p.chromium.launch(executable_path=browser_path, headless=False)
        
        page = browser.new_page()
        try:
            page.goto("https://www.google.com/maps/@19.0482135,73.0710086,16.24z?", timeout=60000)
            page.wait_for_timeout(2000)
            
            page.locator('//input[@id="searchboxinput"]').fill(search_query)
            page.keyboard.press("Enter")
            page.wait_for_timeout(5000)
            
            page.wait_for_selector('//a[contains(@href, "https://www.google.com/maps/place")]')
            
            print("Scrolling to load more business listings...")
            previously_counted = 0
            no_change_count = 0
            max_no_change = 5
            
            while True:
                for scroll_attempt in range(3):
                    page.mouse.wheel(0, random.randint(8000, 15000))
                    page.wait_for_timeout(1000)
                
                page.wait_for_selector('//a[contains(@href, "https://www.google.com/maps/place")]')
                found = page.locator('//a[contains(@href, "https://www.google.com/maps/place")]').count()
                print(f"Currently Found: {found}")
                
                if found < total:
                    time.sleep(2)
                    page.hover('//a[contains(@href, "https://www.google.com/maps/place")]')
                    page.mouse.wheel(0, 10000)
                    found = page.locator('//a[contains(@href, "https://www.google.com/maps/place")]').count()

                if found >= total:
                    print(f"Reached target of {total} places")
                    break
                    
                if found == previously_counted:
                    no_change_count += 1
                    if no_change_count >= max_no_change:
                        print("No new results after multiple attempts. Stopping scroll.")
                        break
                else:
                    no_change_count = 0
                    
                previously_counted = found
                time.sleep(random.uniform(1, 2))

            listings = page.locator('//a[contains(@href, "https://www.google.com/maps/place")]').all()[:total]
            print(f"Total listings to process: {len(listings)}")
            
            for i, listing in enumerate(listings):
                try:
                    print(f"Processing {i+1}/{len(listings)}")
                    
                    listing.click()
                    page.wait_for_timeout(3000)
                    
                    details_loaded = wait_for_business_details(page)
                    
                    if not details_loaded:
                        print("Business details didn't load, skipping...")
                        try:
                            page.keyboard.press("Escape")
                            page.wait_for_timeout(2000)
                        except:
                            pass
                        continue
                    
                    business = extract_business_details(page)
                    
                    # Add keyword and rank to the business object
                    business.keyword = search_query
                    business.rank = i + 1
                    
                    business_id = f"{business.name}_{business.address}"
                    if business.name and business.name != "Unknown Business" and business_id not in seen_businesses:
                        seen_businesses.add(business_id)
                        businesses.append(business)
                        print(f"EXTRACTED: {business.name}")
                        print(f"Type: {business.business_type}")
                        if business.reviews_average:
                            print(f"Rating: {business.reviews_average} ({business.reviews_count} reviews)")
                        print(f"Location: {business.location_area}")
                        print(f"Rank: {business.rank}")
                    else:
                        if business.name == "Unknown Business":
                            print("Invalid business data, skipping...")
                        else:
                            print(f"Duplicate, skipping: {business.name}")
                        
                except Exception as e:
                    print(f"Failed to process listing {i+1}: {e}")
                    try:
                        page.keyboard.press("Escape")
                        page.wait_for_timeout(2000)
                    except:
                        pass
                
                try:
                    page.keyboard.press("Escape")
                    page.wait_for_timeout(2000)
                except:
                    pass
                    
        except Exception as e:
            print(f"Error during scraping: {e}")
        finally:
            browser.close()
    
    print(f"Successfully extracted {len(businesses)} unique businesses")
    return businesses

def save_to_csv_append(businesses: List[Business], output_path: str = "all_businesses.csv"):
    if not businesses:
        print("No data to save")
        return
        
    df = pd.DataFrame([asdict(business) for business in businesses])
    
    column_order = [
        'name', 'business_type', 'location_area', 'address', 
        'google_maps_url', 'website', 'phone_number',
        'reviews_average', 'reviews_count', 'last_3_reviews',
        'opening_hours', 'description', 'keyword', 'rank'  # Added keyword and rank to column order
    ]
    
    existing_columns = [col for col in column_order if col in df.columns]
    remaining_columns = [col for col in df.columns if col not in existing_columns]
    final_column_order = existing_columns + remaining_columns
    
    df = df[final_column_order]
    
    file_exists = os.path.isfile(output_path)
    
    if file_exists:
        df.to_csv(output_path, mode='a', header=False, index=False)
        print(f"Appended {len(df)} businesses to existing file: {output_path}")
    else:
        df.to_csv(output_path, index=False)
        print(f"Created new file with {len(df)} businesses: {output_path}")
    
    print("\nDATA SUMMARY:")
    for col in df.columns:
        non_empty = df[col].notna().sum()
        print(f"{col}: {non_empty}/{len(df)} businesses have data")

def main():
    parser = argparse.ArgumentParser(description="Google Maps Business Scraper")
    parser.add_argument("-s", "--search", type=str, required=True,
                       help="Search query for Google Maps (any business type)")
    parser.add_argument("-t", "--total", type=int, default=20,
                       help="Total number of results to scrape (default: 20)")
    parser.add_argument("-o", "--output", type=str, default="all_business.csv",
                       help="Output CSV file path (default: all_business.csv)")
    
    args = parser.parse_args()
    
    print(f"Starting scrape for: '{args.search}'")
    print(f"Target: {args.total} businesses")
    print(f"Output: {args.output}")
    
    start_time = time.time()
    businesses = scrape_businesses_with_scrolling(args.search, args.total)
    end_time = time.time()
    
    print(f"Total scraping time: {end_time - start_time:.2f} seconds")
    
    save_to_csv_append(businesses, args.output)

if __name__ == "__main__":
    main()