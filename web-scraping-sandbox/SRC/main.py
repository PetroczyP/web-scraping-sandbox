import sys
from scraper import Scraper

def main(url):
    scraper = Scraper(url)
    data = scraper.scrape()
    print(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    main(url)
