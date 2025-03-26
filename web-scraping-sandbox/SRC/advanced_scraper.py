import requests
import time
import random
from bs4 import BeautifulSoup

class AdvancedScraper:
    def __init__(self, url):
        self.url = url
        # More comprehensive browser-like headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'TE': 'Trailers',
        }
        # Add a session to maintain cookies
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def fetch_content(self, max_retries=3):
        # Add a random delay to mimic human behavior
        time.sleep(random.uniform(1, 3))
        
        for attempt in range(max_retries):
            try:
                print(f"Attempt {attempt + 1} to fetch {self.url}")
                response = self.session.get(self.url)
                response.raise_for_status()
                return response.content
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 403 and attempt < max_retries - 1:
                    print(f"Received 403 Forbidden. Retrying in {2 ** attempt} seconds...")
                    time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    print(f"Error: {e}")
                    # Return the content anyway, even with the error
                    return e.response.content
            except Exception as e:
                print(f"Unexpected error: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    return None

    def parse_content(self, content):
        if content:
            soup = BeautifulSoup(content, 'lxml')
            return soup
        return None

    def scrape(self):
        content = self.fetch_content()
        parsed_content = self.parse_content(content)
        return parsed_content