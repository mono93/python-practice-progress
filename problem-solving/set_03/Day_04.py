"""
 Challenge: Download Cover Images of First 10 Books

Goal:
- Visit https://books.toscrape.com/
- Scrape the first 10 books listed on the homepage
- For each book, extract:
  • Title
  • Image URL

Then:
- Download each image
- Save it to a local `images/` folder with the filename as the book title (sanitized)

Example:
 Title: "A Light in the Attic"
 Saved as: images/A_Light_in_the_Attic.jpg

Bonus:
- Handle invalid filename characters
- Show download progress
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = "https://books.toscrape.com/"
BOOKS_TO_SCRAPE = 10
IMAGE_DIR = "images"

def sanitize_filename(name):
    return re.sub(r'[^\w\-_. ]', '', name).replace(" ", "_")

def download_image(url, filename):
    try:
        response = requests.get(url, stream=True, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Check if the request was successful
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)
        print(f"✅ Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {filename}: {e}")

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
        download_image(image_url, filename)
    

if __name__ == "__main__":
    main()