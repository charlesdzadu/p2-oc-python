
    
import csv
import sys
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
    
    
if __name__ == "__main__":
    """Main function"""
    
    args = sys.argv[1:]
    if not args:
        single_category_url = "https://books.toscrape.com/catalogue/category/books/young-adult_21/index.html"
        csv_file_path = "assets/single_category_data.csv"
    else:
        if len(args) == 1:
            single_category_url = args[0]
            csv_file_path = "assets/single_category_data.csv"
        elif len(args) == 2:
            single_category_url = args[0]
            csv_file_path = args[1]
        else:
            print("Please provide 1 or 2 arguments: Category url and a csv file path")
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
    
    print("Scraping Single Category \n")
    
    with open(csv_file_path, "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(headers)
    
    scrape_single_category(single_category_url, csv_file_path)
    
    
    print("Scraping Single Category End \n")