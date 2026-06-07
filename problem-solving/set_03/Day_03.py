"""
 Challenge: Scrape Books To Scrape (70 Books)

Goal:
- Visit https://books.toscrape.com/
- Scrape each book's:
  • Title 
  • Price 

You must:
- Crawl through multiple pages using the "next" button until you collect 70 books.
- Save the data to a JSON file: books_data.json
- Handle network errors gracefully.

Bonus:
- Track how many books scraped
- Print progress as you collect pages
"""

import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
BOOKS_TO_SCRAPE = 70
START_PAGE = "catalogue/page-1.html"
OUTPUT_FILE = "books_data.json"

def scrape_books(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return [], None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select("article.product_pod")
    books = []

    for article in articles:
        title = article.h3.a['title']
        price = article.select_one('p.price_color').get_text(strip=True)
        books.append({'Title': title, 'Price': price})

    next_link = soup.select_one("li.next > a")
    next_url = urljoin(BASE_URL, next_link['href']) if next_link else None

    return books, next_url

def main():
    collected_books = []
    current_url = urljoin(BASE_URL, START_PAGE)
    
    while len(collected_books) < BOOKS_TO_SCRAPE and current_url:
        print(f"Scraping: {current_url}")
        books, next_url = scrape_books(current_url)
        collected_books.extend(books)
        current_url = next_url
    
    collected_books = collected_books[:BOOKS_TO_SCRAPE]  # Limit to 70 books
    print(f"Total books collected: {len(collected_books)}")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(collected_books, f, ensure_ascii=False, indent=4)
    print(f"✅ Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
