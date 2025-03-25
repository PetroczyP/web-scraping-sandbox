import pytest
from SRC.scraper import Scraper

@pytest.fixture
def scraper():
    url = "https://example.com"
    return Scraper(url)

def test_fetch_content(scraper, requests_mock):
    requests_mock.get(scraper.url, text="Mocked content")
    content = scraper.fetch_content()
    assert content == b"Mocked content"

def test_parse_content(scraper):
    content = b"<html><body><h1>Test</h1></body></html>"
    parsed_content = scraper.parse_content(content)
    assert parsed_content.find("h1").text == "Test"

def test_scrape(scraper, requests_mock):
    requests_mock.get(scraper.url, text="<html><body><h1>Test</h1></body></html>")
    parsed_content = scraper.scrape()
    assert parsed_content.find("h1").text == "Test"
