from flask import Flask, request, jsonify
from scraper import Scraper
from utils import extract_emails, extract_phone_numbers, clean_text

app = Flask(__name__)

@app.route('/api/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    additional_info = data.get('additional_info')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    scraper = Scraper(url)
    soup = scraper.scrape()

    if not soup:
        return jsonify({'error': 'Failed to scrape the website'}), 500

    title = soup.title.text if soup.title else "No title found"
    all_text = soup.get_text()
    emails = extract_emails(all_text)
    phone_numbers = extract_phone_numbers(all_text)
    cleaned_text_sample = clean_text(all_text[:200])

    result = {
        'title': title,
        'emails': emails,
        'phone_numbers': phone_numbers,
        'cleaned_text_sample': cleaned_text_sample
    }

    if additional_info:
        # Add logic to handle additional information if needed
        result['additional_info'] = additional_info

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
