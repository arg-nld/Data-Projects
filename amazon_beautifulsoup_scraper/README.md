# Amazon Best Sellers Scraper

A Python web scraping automation tool that extracts real-time ranking data from Amazon's Best Sellers directory and structures it for data analysis.

### 🛠️ Tech Stack
* **Python 3**
* **Requests & BeautifulSoup4** (HTTP fetching and HTML parsing)
* **Pandas** (Data cleaning, structuring, and export)

### 📊 Key Features
* **Anti-Bot Evasion:** Utilizes custom `User-Agent` headers to successfully bypass basic automated request blocks (HTTP 503).
* **Dynamic DOM Handling:** Implements `try/except` logic and fallback HTML targeting (e.g., extracting titles from image `alt` attributes) to maintain stability despite Amazon's frequent UI layout tests.
* **Automated Data Cleaning:** Uses Pandas (`fillna()`) to detect and clean missing values (`NaN`) caused by HTML variances in Kindle Unlimited or Audiobook listings.
* **Pipeline Export:** Parses raw HTML directly into a structured Pandas DataFrame and exports a clean `.csv` file ready for business intelligence tools.