"""
 Challenge: Download Cover Images Using wget

Goal:
- Scrape https://books.toscrape.com/
- Collect the first 10 books on the homepage
- Extract the title and image URL for each book
- Use the `wget` library to download and save images in a folder called 'images/'
- Use book titles (sanitized) as image filenames

Bonus:
- Add progress for each download
- Ensure folder is created if it doesn't exist
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import wget

BASE_URL = "https://books.toscrape.com/"
BOOKS_TO_SCRAPE = 10
IMAGE_DIR = "images_1"

def sanitize_filename(name):
    return re.sub(r'[^\w\-_. ]', '', name).replace(" ", "_")

def main():
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    try:
        response = requests.get(BASE_URL, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return 
    
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.select("article.product_pod")[:BOOKS_TO_SCRAPE]
    for book in books:
        title = book.h3.a['title']
        image_url = urljoin(BASE_URL, book.img['src'])
        filename = os.path.join(IMAGE_DIR, sanitize_filename(title) + ".jpg")
        # This code uses wget to download the image and save it with the sanitized book title as the filename
        # but it is currently commented out. Uncomment the line below to enable image downloading.
        wget.download(image_url, filename)

if __name__ == "__main__":
    main()