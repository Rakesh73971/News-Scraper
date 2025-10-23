import requests
from bs4 import BeautifulSoup

from datetime import datetime


def scrape_news_headlines():
    """
    Scrape top headlines from BBC News and save to a text file
    """
    try:
        # BBC URL
        url = "https://www.bbc.com/news"
        
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print("Fetching news from BBC...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        headlines = []
        
        
        selectors = [
            'h2[data-testid="card-headline"]',
            'h3[data-testid="card-headline"]',
            '.gs-c-promo-heading__title',
            '.gs-c-promo-heading',
            'h2 a',
            'h3 a'
        ]
        
        for selector in selectors:
            elements = soup.select(selector)
            for element in elements:
               
                text = element.get_text(strip=True)
                if text and len(text) > 10: 
                    headlines.append(text)
        
       
        seen = set()
        unique_headlines = []
        for headline in headlines:
            if headline not in seen:
                seen.add(headline)
                unique_headlines.append(headline)
        
        
        top_headlines = unique_headlines[:20]
        
        if not top_headlines:
            print("No headlines found. The website structure might have changed.")
            return
        
      
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"news_headlines_{timestamp}.txt"
        
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("TOP NEWS HEADLINES\n")
            file.write("=" * 50 + "\n")
            file.write(f"Scraped on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Source: BBC News\n")
            file.write("=" * 50 + "\n\n")
            
            for i, headline in enumerate(top_headlines, 1):
                file.write(f"{i}. {headline}\n")
        
        print(f"Successfully scraped {len(top_headlines)} headlines!")
        print(f"Headlines saved to: {filename}")
        
        
        print("\nFirst 5 headlines:")
        for i, headline in enumerate(top_headlines[:5], 1):
            print(f"{i}. {headline}")
        
        return filename
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    print("BBC News Headlines Scraper")
    print("=" * 30)
    

    result = scrape_news_headlines()
    
    if result:
        print(f"\nScraping completed successfully!")
        print(f"Check the file: {result}")
    else:
        print("\nFailed to scrape headlines from BBC News.")
        print("This might be due to:")
        print("- Network connectivity issues")
        print("- Website structure changes")
        print("- Anti-scraping measures")
