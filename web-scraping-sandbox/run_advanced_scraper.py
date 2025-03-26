import sys
from SRC.advanced_scraper import AdvancedScraper
from SRC.utils import extract_emails, extract_phone_numbers, clean_text

def main(url):
    print(f"Scraping URL: {url}")
    
    # Initialize and run the advanced scraper
    scraper = AdvancedScraper(url)
    soup = scraper.scrape()
    
    if not soup:
        print("Failed to scrape the website.")
        return
    
    # Extract and print the title
    title = soup.title.text if soup.title else "No title found"
    print(f"\nPage Title: {title}")
    
    # Extract all text from the page
    all_text = soup.get_text()
    
    # Extract emails
    emails = extract_emails(all_text)
    if emails:
        print("\nEmails found:")
        for email in emails:
            print(f"- {email}")
    else:
        print("\nNo emails found.")
    
    # Extract phone numbers
    phone_numbers = extract_phone_numbers(all_text)
    if phone_numbers:
        print("\nPhone numbers found:")
        for phone in phone_numbers:
            print(f"- {phone}")
    else:
        print("\nNo phone numbers found.")
    
    # Print a sample of cleaned text
    print(f"\nSample cleaned text (first 200 characters): {clean_text(all_text[:200])}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_advanced_scraper.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    main(url)