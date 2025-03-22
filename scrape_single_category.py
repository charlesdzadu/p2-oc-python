
    
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

from scrape_single_page import scrape_single_page


def scrape_single_category(url: str, file_path: str = None):
    """Scrape a single category"""
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    products_links = []
    total_products = int(soup.find("form", {"class": "form-horizontal"}).find("strong").text)
    
    category_name = soup.find("h1").text
    
    
    print(f"Category: {category_name} - Total products: {total_products}")
    
    
    print("Checking products total...")
    while len(products_links) < total_products:
        lis = soup.find("ol", {"class": "row"}).find_all("li")
        for li in lis:
            products_links.append(li.find("a")["href"])
            
        pager = soup.find("ul", {"class": "pager"})
        if pager:
            next_page = pager.find("li", {"class": "next"})
            if next_page:
                next_page_url = next_page.find("a")["href"]
                url = urljoin(url, next_page_url)
                res = requests.get(url)
                soup = BeautifulSoup(res.text, "html.parser")
            else:
                break
        else:
            break
        
    print(f"Starting scraping {len(products_links)} products...")
    treated_products = 0
    for product_link in products_links:
        product_url = urljoin(url, product_link)
        scrape_single_page(product_url, file_path)
        treated_products += 1
        percentage = round((treated_products / total_products) * 100, 2)
        print(f"Scraping products: {percentage}%")
    
    
    return True
    