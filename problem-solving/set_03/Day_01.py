"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup


def scrape_wikipedia_headers(url):
    try:
        response = requests.get(
            url, headers={"User-Agent": "Mozilla/5.0", "X-Attempt-Count": "120"})
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    headers = []
    h2_tags = soup.find_all('h2')
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)
        if header_text and header_text.lower() != 'contents':  # Skip the "Contents" header
            headers.append(header_text)

    print(headers)


if __name__ == "__main__":
    wikipedia_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    scrape_wikipedia_headers(wikipedia_url)
