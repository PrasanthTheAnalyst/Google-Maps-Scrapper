# Google Maps Business Scraper 🗺️
<div align="center">




![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

**⚠️ EDUCATIONAL PURPOSE ONLY** - For research and learning purposes

A powerful automated tool to extract comprehensive business information from Google Maps

[Installation](#-installation) • [Usage](#-usage) • [Features](#-features) • [Disclaimer](#-important-disclaimer)

</div>

## 📋 Overview

Google Maps Business Scraper is a sophisticated Python tool that automatically extracts detailed business information from Google Maps search results. It efficiently collects comprehensive data including contact details, reviews, ratings, and location information for multiple businesses.

## ✨ Features

- **📊 Complete Business Profiles**: Extract name, address, website, phone number, and Google Maps URL
- **⭐ Review Analytics**: Capture average rating, review count, and latest 3 reviews with excerpts
- **📍 Location Intelligence**: Area analysis, business type categorization, and opening hours
- **🏆 Rank Tracking**: Monitor position in search results for each business
- **🔄 Batch Processing**: Scrape multiple businesses in single search queries
- **💾 CSV Export**: Append results to existing files for continuous data collection
- **🖱️ Auto-Scrolling**: Automatic pagination handling and intelligent scroll simulation
- **🛡️ Robust Error Handling**: Comprehensive error recovery and duplicate detection

## 🚨 Important Disclaimer

> **⚠️ EDUCATIONAL USE ONLY**
> 
> This tool is developed **strictly for educational and research purposes**. Users are solely responsible for:
> - Complying with Google's Terms of Service
> - Adhering to local laws and regulations
> - Respecting robots.txt and rate limiting
> - Obtaining proper authorization for data collection
> - Implementing appropriate delays between requests
> 
> **The developer is not liable for any misuse, damages, or legal violations resulting from this software. Use at your own risk and responsibility.**

## 📥 Installation

### Prerequisites
- Python 3.7 or higher
- Google Chrome browser installed

## 📥 Installation

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/PrasanthTheAnalyst/Google-Maps-Scrapper.git
cd Google-Maps-Scrapper
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers**
```bash
playwright install chromium
```

## 🚀 Usage
**Basic Command Line Usage**

# Scrape 20 restaurants in New York
```bash
python app.py -s "restaurants in New York" -t 20 -o "nyc_restaurants.csv"
```

# Scrape 50 coffee shops in London
```bash
python app.py -s "coffee shops London" -t 50 -o "london_coffee.csv"
```

# Scrape 30 hotels in Tokyo
```bash
python app.py -s "hotels Tokyo Japan" -t 30 -o "tokyo_hotels.csv"
```

**Advanced Usage Examples**
# Scrape specific business types
```bash
python app.py -s "digital marketing agencies San Francisco" -t 25 -o "agencies.csv"
```

# Extract local service providers
```bash
python app.py -s "plumbers near me" -t 15 -o "local_plumbers.csv"
```

# Research competitors in area
```bash
python app.py -s "coffee shops near Manhattan" -t 40 -o "competitor_analysis.csv"
```

**Command Line Arguments**

| Argument | Description | Default | Required |
|:---------|:------------|:--------|:--------:|
| `-s, --search` | Search query for Google Maps | - | **Yes** |
| `-t, --total` | Number of businesses to scrape | 20 | No |
| `-o, --output` | Output CSV file path | `"all_business.csv"` | No |

**Python Script Integration**
from app import scrape_businesses_with_scrolling, save_to_csv_append

# Scrape businesses programmatically
businesses = scrape_businesses_with_scrolling(
    search_query="restaurants in downtown",
    total=25
)

# Save to CSV
save_to_csv_append(businesses, "restaurant_data.csv")

print(f"Successfully extracted {len(businesses)} businesses")

📊 Output Data Structure
The scraper generates CSV files with comprehensive business information:

| Column | Description | Example |
|--------|-------------|---------|
| `name` | Business name | "Starbucks Coffee" |
| `business_type` | Type of business | "Coffee shop" |
| `location_area` | General area/landmark | "Near Central Park" |
| `address` | Full physical address | "123 Main St, New York, NY" |
| `website` | Business website URL | "https://starbucks.com" |
| `phone_number` | Contact phone number | "+1-555-0123" |
| `reviews_average` | Average rating (1-5) | 4.5 |
| `reviews_count` | Total number of reviews | 1250 |
| `last_3_reviews` | Recent review excerpts | "Great coffee!... Friendly staff..." |
| `opening_hours` | Business operating hours | "Open ⋅ Closes 9 PM" |
| `google_maps_url` | Direct Google Maps link | "https://maps.google.com/place/..." |
| `keyword` | Original search query | "coffee shops nyc" |
| `rank` | Search result position | 3 |
| `description` | Business description | "Coffee shop chain known for..." |

**🛠️ Technical Architecture**

**Core Components**

**Playwright:** Advanced browser automation and interaction

**Pandas:** Efficient data manipulation and CSV export

**Python Dataclasses:** Structured data handling and type safety

**Argparse:** Robust command-line interface implementation

**Data Extraction Methodology**
XPath-based element selection and traversal

Intelligent scrolling for pagination handling

Error-resistant text extraction with fallback mechanisms

Smart duplicate business detection

Efficient review excerpt processing

**🤝 Contributing**

We welcome contributions from the community! Please feel free to submit pull requests, report bugs, or suggest new features.

**Fork the repository**

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

**Development Setup**

# Install development dependencies

pip install -r requirements.txt

pip install black flake8 pytest

# Run code formatting

black app.py

# Run linting

flake8 app.py

**📝 License**

This project is licensed under the MIT License - see the LICENSE file for details.

**
☕ Support the Project**
If you find this tool helpful for your educational or research projects, consider supporting its development:

**Buy Me a Coffee:** [https://buymeacoffee.com/prasanthanalyst](https://buymeacoffee.com/prasanththeanalyst)

**Your support helps:**

🐛 Fix bugs and maintain the tool

📚 Create educational content and tutorials

🚀 Develop new features and improvements

💻 Cover hosting and development costs

⚠️ Ethical Usage Guidelines

🕐 Implement respectful delays between requests (2-5 seconds)

🔍 Use for legitimate academic and research purposes only

📚 Educational and non-commercial use encouraged

🚫 Do not overload or disrupt Google's services

📉 Limit scraping frequency and volume appropriately

✅ Always check robots.txt and terms of service

🛡️ Respect website policies and rate limits

**🆘 Troubleshooting**

**Common Issues & Solutions**

**"Chrome not found" error**

Ensure Google Chrome is installed on your system

Update the browser_path in app.py if needed for your OS

**"No businesses found" or timeout errors**

Check your internet connection stability

Verify the search query works manually in Google Maps

Try different, more specific search terms

Increase timeout values in the code if needed

**Playwright installation issues**

# Reinstall Playwright if needed

pip uninstall playwright

pip install playwright

playwright install chromium

**Memory or performance issues**

Reduce the --total parameter value

Add longer delays between requests

Run during off-peak hours

**Getting Help**

📋 Check Issues for existing solutions

💬 Start a Discussion for questions

🐛 Report bugs with detailed error messages and system information

🔄 Changelog

Version 1.0

Initial release with core scraping functionality

Business profile data extraction

Review and rating collection

CSV export capabilities

<div align="center">
    
**Developed by Prasanth The Analyst**

Creating tools for educational and research purposes

Remember: Always use web scraping responsibly and ethically

https://img.shields.io/github/followers/PrasanthTheAnalyst?style=social

</div> ```


