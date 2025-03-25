# Web Scraping Sandbox

## Project Description and Purpose

The Web Scraping Sandbox is a modular and extensible web scraping framework designed to simplify the process of extracting data from websites. It provides a set of tools and utilities to facilitate web scraping tasks, including making HTTP requests, parsing HTML content, and handling various web scraping scenarios.

## Setup Instructions

### Prerequisites

- Python 3.11 or higher
- Docker (optional, for containerized setup)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/githubnext/web-scraping-sandbox.git
   cd web-scraping-sandbox
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Docker Setup

1. Build the Docker image:

   ```bash
   docker build -t web-scraping-sandbox .
   ```

2. Run the Docker container:

   ```bash
   docker run -it --rm web-scraping-sandbox
   ```

## Running Tests

To run the unit tests using pytest, execute the following command:

```bash
pytest
```

## Example Usage

Here's an example of how to use the web scraper:

1. Create a Python script (e.g., `example.py`) with the following content:

   ```python
   from SRC.scraper import Scraper

   url = "https://example.com"
   scraper = Scraper(url)
   data = scraper.scrape()
   print(data)
   ```

2. Run the script:

   ```bash
   python example.py
   ```
