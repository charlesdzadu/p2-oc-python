
import csv
import sys
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

from scrape_single_category import scrape_single_category


def scrape_all_categories(url: str, file_path: str = None):
    """Scrape all categories"""
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    
    categories_links = []
    lis = soup.find("ul", {"class": "nav nav-list"}).find("li").find("ul").find_all("li")
    for li in lis:
        category_url = urljoin(url, li.find("a")["href"])
        categories_links.append(category_url)
        
    print(f"Found {len(categories_links)} categories\n")
    
    treated_categories = 0
    for category_url in categories_links:
        treated_categories += 1
        percentage = round((treated_categories / len(categories_links)) * 100, 2)
        print(f"\nScraping categories: {percentage}% - {treated_categories}/{len(categories_links)} \n")
        scrape_single_category(category_url, file_path)
        
    return True
    
    
    
if __name__ == "__main__":
    """Main function"""
    args = sys.argv[1:]
    website_url = "https://books.toscrape.com/index.html"
    csv_file_path = "assets/books_data.csv"
    
    if not args:
        pass
    else:
        if len(args) == 1:
            csv_file_path = args[0]
        else:
            print("Please provide 1 argument: csv file path")
            sys.exit(1)
            
            
    headers = [
        "product_page_url", 
        "universal_product_code", 
        "title",
        "price_including_tax", 
        "price_excluding_tax", 
        "number_available", 
        "product_description", 
        "category", 
        "review_rating", 
        "image_url"
    ]
    
    print("Scraping Books Website \n")
    
    with open(csv_file_path, "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(headers)
    
    scrape_all_categories(website_url, csv_file_path)
    
    
    print("Scraping Books Website End \n")
    
