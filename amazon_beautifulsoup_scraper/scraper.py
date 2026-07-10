import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
URL = "https://www.amazon.com/gp/bestsellers/books/"

# User-Agent header to prevent immediate blocking from Amazon
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def scrape_amazon_books():
    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    book_cards = soup.find_all("div", id="gridItemRoot")
    scraped_books = []

    for card in book_cards:
        # 1. Extract Rank
        rank_tag = card.find("span", class_="zg-bdg-text")
        rank = rank_tag.text.replace("#", "").strip() if rank_tag else None
        
        # 2. Extract Title
        title_img = card.find("img")
        title = title_img.get("alt").strip() if title_img else None
        
        # 3. Extract Author
        author_div = card.find("div", class_="a-row a-size-small")
        author = author_div.text.strip() if author_div else None
        
        # 4. Extract Price
        price_span = card.find("span", class_="p13n-sc-price")
        price = price_span.text.strip() if price_span else None

        # Only append if we successfully grabbed the core data
        if title and rank:
            scraped_books.append({
                "Rank": int(rank),
                "Title": title,
                "Author": author,
                "Price": price
            })

    # Create the DataFrame
    df = pd.DataFrame(scraped_books)
    
    # --- DATA CLEANING STEP ---
    # Replace all NaN (missing) prices with "Format Variance / Not Listed"
    df["Price"] = df["Price"].fillna("Not Listed")
    
    # Sort and reset index
    df = df.sort_values(by="Rank").reset_index(drop=True)
    
    print("\n--- AMAZON BEST SELLING BOOKS ---")
    print(df)
    
    # Export to CSV
    df.to_csv("amazon_bestsellers.csv", index=False)
    print("\nSuccess! Cleaned data exported to amazon_bestsellers.csv")

if __name__ == "__main__":
    scrape_amazon_books()