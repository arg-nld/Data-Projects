# Amazon Best Sellers Scraper & Cleaner



A Python-based web scraper that extracts real-time ranking data from Amazon's Book Best Sellers page. The script handles standard anti-bot protections, cleans up inconsistent data layout formats, and exports a structured CSV file ready for downstream analysis.



### 🛠️ Tech Stack

* **Python 3**

* **Requests** (HTTP page fetching)

* **BeautifulSoup4** (HTML parsing)

* **Pandas** (Data cleaning and CSV structuring)



---



### 💡 Key Challenges & Solutions



Building a stable scraper for Amazon requires handling a few real-world edge cases. Here is how this script addresses them:



* **Bypassing the Bot Wall:** Amazon aggressively blocks automated Python scripts with 503 errors. This script uses a custom `User-Agent` header to mimic a standard desktop browser configuration, ensuring reliable page delivery.

* **Resilient Title Extraction:** Amazon frequently tweaks its UI elements and text classes. To keep the script from breaking, the parser pulls book titles directly from the image asset's `alt` description tag—a reliable anchor that Amazon leaves intact for accessibility and SEO.

* **Handling Missing Prices (`NaN` Values):** Kindle Unlimited books, pre-orders, and audiobooks use completely different HTML layers than standard paperback prices. Instead of letting these variations crash the script or leave ugly blank gaps, the pipeline utilizes Pandas' `.fillna()` function to cleanly flag unlisted prices as `"Not Listed"`.



---



### 🚀 How to Run



1. Clone this repository and navigate to the folder:

   ```bash

   cd amazon_beautifulsoup_scraper