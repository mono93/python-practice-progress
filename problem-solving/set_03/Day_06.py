"""
 Challenge: Quote of the Day Image Maker

Goal:
- Scrape random quotes from https://quotes.toscrape.com/
- Extract quote text and author for the first 5 quotes
- Create an image for each quote using PIL
- Save images in 'quotes/' directory using filenames like quote_1.png, quote_2.png, etc.


"""

import os
import textwrap
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "quotes"
QUOTES_TO_SCRAPE = 5


def scrape_quotes(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []

    extracted_quotes = []
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.select("div.quote")

    for quote in quotes[:QUOTES_TO_SCRAPE]:
        text = quote.select_one("span.text").get_text(strip=True)
        author = quote.select_one("small.author").get_text(strip=True)
        extracted_quotes.append({"text": text, "author": author})

    return extracted_quotes


def create_quote_image(quote, author, index):
    print(f"Creating image for quote {index}: '{quote}' by {author}")
    width, height = 800, 400
    background_color = "#f8d77f"
    text_color = "#262626"

    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    wrapped = textwrap.fill(quote, width=60)
    author_text = f"- {author}"

    y_text = 60
    draw.text((40, y_text), wrapped, font=font, fill=text_color)
    y_text += wrapped.count('\n') * 15 + 40
    draw.text((500, y_text), author_text, font=font, fill=text_color)

    # save image
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filename = os.path.join(OUTPUT_DIR, f"quote_{index}.png")
    image.save(filename)
    print(f"✅ saved: {filename}")


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    quotes = scrape_quotes(BASE_URL)

    for idx, quote in enumerate(quotes, start=1):
        create_quote_image(quote["text"], quote["author"], idx)


if __name__ == "__main__":
    main()
