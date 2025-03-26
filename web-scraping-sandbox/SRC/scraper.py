import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url
        # Add user-agent headers to mimic a browser
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

    def fetch_content(self):
        response = requests.get(self.url, headers=self.headers)
        response.raise_for_status()
        return response.content

    def parse_content(self, content):
        soup = BeautifulSoup(content, 'lxml')
        return soup

    def scrape(self):
        content = self.fetch_content()
        parsed_content = self.parse_content(content)
        return parsed_content