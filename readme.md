Google Maps Business Scraper
<div align="center">
https://img.shields.io/badge/Python-3.7+-blue.svg
https://img.shields.io/badge/Playwright-Automation-green.svg
https://img.shields.io/badge/License-MIT-yellow.svg

⚠️ EDUCATIONAL PURPOSE ONLY - For research and learning purposes

A powerful automated tool to extract comprehensive business information from Google Maps

Installation • Usage • Features • Disclaimer

</div>
📋 Overview
Google Maps Business Scraper is a Python-based tool that automatically extracts detailed business information from Google Maps search results. It collects comprehensive data including contact details, reviews, ratings, and location information for multiple businesses simultaneously.

✨ Features
📊 Complete Business Profiles: Name, address, website, phone number, Google Maps URL

⭐ Review Analytics: Average rating, review count, latest 3 reviews with excerpts

📍 Location Intelligence: Area analysis, business type categorization, opening hours

🏆 Rank Tracking: Position in search results for each business

🔄 Batch Processing: Scrape multiple businesses in single search query

💾 CSV Export: Append results to existing files for continuous data collection

🖱️ Auto-Scrolling: Automatic pagination handling and scroll simulation

🛡️ Error Handling: Robust error recovery and duplicate detection

🚨 Important Disclaimer
⚠️ EDUCATIONAL USE ONLY

This tool is developed strictly for educational and research purposes. Users are solely responsible for:

Complying with Google's Terms of Service

Adhering to local laws and regulations

Respecting robots.txt and rate limiting

Obtaining proper authorization for data collection

The developers are not liable for any misuse, damages, or legal violations resulting from this software. Use at your own risk.

📥 Installation
Prerequisites
Python 3.7 or higher

Google Chrome browser installed

Step-by-Step Setup
Clone the repository

bash
git clone https://github.com/PrasanthTheAnalyst/google-maps-scraper.git
cd google-maps-scraper
Create virtual environment (recommended)

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Install Playwright browsers

bash
playwright install chromium
🚀 Usage
Basic Command Line Usage
bash
# Scrape 20 restaurants in New York
python app.py -s "restaurants in New York" -t 20 -o "nyc_restaurants.csv"

# Scrape 50 coffee shops in London
python app.py -s "coffee shops London" -t 50 -o "london_coffee.csv"

# Scrape 30 hotels in Tokyo
python app.py -s "hotels Tokyo Japan" -t 30 -o "tokyo_hotels.csv"
Command Line Arguments
Argument	Description	Default
-s, --search	Search query for Google Maps	Required
-t, --total	Number of businesses to scrape	20
-o, --output	Output CSV file path	"all_business.csv"
Python Script Usage
python
from app import scrape_businesses_with_scrolling, save_to_csv_append

# Scrape businesses programmatically
businesses = scrape_businesses_with_scrolling(
    search_query="digital marketing agencies San Francisco",
    total=25
)

# Save to CSV
save_to_csv_append(businesses, "marketing_agencies.csv")
📊 Sample Output
The scraper generates CSV files with the following columns:

Column	Description	Example
name	Business name	"Starbucks Coffee"
business_type	Type of business	"Coffee shop"
location_area	General area/landmark	"Near Central Park"
address	Full address	"123 Main St, New York, NY"
website	Business website	"https://starbucks.com"
phone_number	Contact phone	"+1-555-0123"
reviews_average	Average rating	4.5
reviews_count	Total reviews	1250
last_3_reviews	Recent review excerpts	"Great coffee!... Friendly staff..."
opening_hours	Business hours	"Open ⋅ Closes 9 PM"
google_maps_url	Direct Maps link	"https://maps.google.com/place/..."
keyword	Search query used	"coffee shops nyc"
rank	Search result position	3
🛠️ Technical Details
Architecture
Playwright: For browser automation and interaction

Pandas: For data manipulation and CSV export

Dataclasses: For structured data handling

Argparse: For command-line interface

Data Extraction Methods
XPath-based element selection

Smart scrolling for pagination

Error-resistant text extraction

Duplicate business detection

Review excerpt processing

🤝 Contributing
We welcome contributions! Please feel free to submit pull requests, report bugs, or suggest new features.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

☕ Support the Project
If you find this tool helpful for your educational or research projects, consider supporting its development:


Buy Me a Coffee: https://buymeacoffee.com/prasanththeanalyst

Your support helps maintain and improve this educational tool!

⚠️ Responsible Usage Guidelines
🕐 Respect rate limits - add delays between requests

🔍 Use for legitimate research purposes only

📚 Educational and academic use encouraged

🚫 Do not overload Google's servers

📉 Limit scraping frequency and volume

✅ Check robots.txt before scraping any website

🆘 Troubleshooting
Common Issues
"Chrome not found" error

Ensure Google Chrome is installed

Update the browser_path in app.py if needed

"No businesses found"

Check your internet connection

Verify the search query works manually in Google Maps

Try different search terms

Playwright installation issues

bash
python -m pip install --upgrade pip
pip uninstall playwright
pip install playwright
playwright install
📞 Support
For educational support and questions:

Create an Issue

Check existing discussions in Discussions

<div align="center">
Remember: This tool is for educational purposes only. Always respect terms of service and legal boundaries.

</div>