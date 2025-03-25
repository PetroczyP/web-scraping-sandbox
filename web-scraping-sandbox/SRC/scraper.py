import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url

    def fetch_content(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content

    def parse_content(self, content):
        soup = BeautifulSoup(content, 'lxml')
        return soup

    def scrape(self):
        content = self.fetch_content()
        parsed_content = self.parse_content(content)
        return parsed_content
