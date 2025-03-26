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

### Setting Up and Running the React UI

1. Navigate to the `web-scraping-sandbox/ui` directory:

   ```bash
   cd web-scraping-sandbox/ui
   ```

2. Install the dependencies:

   ```bash
   npm install
   ```

3. Start the React development server:

   ```bash
   npm start
   ```

4. Open your browser and navigate to `http://localhost:3000` to access the UI.

### Running the Docker Container with the UI

1. Build the Docker image:

   ```bash
   docker build -t web-scraping-sandbox .
   ```

2. Run the Docker container:

   ```bash
   docker run -it --rm -p 3000:3000 -p 5000:5000 web-scraping-sandbox
   ```

3. Open your browser and navigate to `http://localhost:3000` to access the UI.

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
