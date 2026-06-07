"""
 Challenge: Hacker News Top Posts Scraper

Build a Python script that:
1. Fetches the HN homepage (news.ycombinator.com).
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
   - Title
   - URL
4. Handles network errors and uses a clean CSV structure.
"""

import requests
import csv
from bs4 import BeautifulSoup

def scrape_hacker_news_top_posts(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []
    
    posts = []
    soup = BeautifulSoup(response.text, 'html.parser')
    post_links = soup.select("span.titleline > a")[:20]  # Get the top 20 post links

    for link in post_links:
        title = link.get_text(strip=True)
        url = link['href']
        posts.append({'Title': title, 'URL': url})

    return posts

def save_to_csv(data, filename):
    if not data:
        print("No data to save.")
        return
    
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Data saved to {filename}")

if __name__ == "__main__":
    hn_url = "https://news.ycombinator.com/"
    posts = scrape_hacker_news_top_posts(hn_url)
    save_to_csv(posts, 'hn_top20.csv')