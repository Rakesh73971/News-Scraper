# BBC News Headlines Scraper

A Python script that scrapes top headlines from BBC News and saves them to a text file.

## Features

- Scrapes headlines from BBC News
- Saves headlines with timestamp to text files
- Handles duplicate headlines
- Includes error handling
- User-agent headers to avoid blocking

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the scraper:
```bash
python news_scraper.py
```

The script will:
1. Scrape headlines from BBC News
2. Save headlines to a timestamped text file
3. Display the first 5 headlines in the console

## Output

The script creates text files with names like:
- `news_headlines_20241201_143022.txt`

Each file contains:
- Header with scraping timestamp and source
- Numbered list of headlines
- Clean, readable format

## Notes

- The script includes proper headers to mimic a real browser
- It handles various HTML structures and selectors
- Duplicate headlines are automatically removed
- Limited to top 20 headlines to avoid overwhelming output
- Focuses solely on BBC News for reliable, consistent results
