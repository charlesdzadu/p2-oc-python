
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
        scrape_single_category(category_url, file_path)
        treated_categories += 1
        percentage = round((treated_categories / len(categories_links)) * 100, 2)
        print(f"Scraping categories: {percentage}% - {treated_categories}/{len(categories_links)} \n")
        
    return True
    
    
    
