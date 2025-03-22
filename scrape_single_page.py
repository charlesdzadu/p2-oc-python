import csv
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

from helpers import clean_text

def scrape_single_page(url: str, file_path: str = None) -> dict:
    """Scrape a single page"""
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    product_page_url = url
    universal_product_code = clean_text(soup.find("th", string="UPC").find_next("td").text)
    title = clean_text(soup.find("h1").text)
    price_including_tax = clean_text(soup.find("th", string="Price (incl. tax)").find_next("td").text)
    price_excluding_tax = clean_text(soup.find("th", string="Price (excl. tax)").find_next("td").text)
    number_available = clean_text(soup.find("th", string="Availability").find_next("td").text)
    product_description_id = soup.find("div", {"id": "product_description"})
    if product_description_id:
        product_description = clean_text(product_description_id.find_next("p").text)
    else:
        product_description = ""
    
    category = clean_text(soup.find("ul", {"class": "breadcrumb"}).find_all("li")[-2].text)
    review_rating = clean_text(soup.find("th", string="Number of reviews").find_next("td").text)
    image_url = soup.find("div", {"class": "item active"}).find("img")["src"]
    image_url = urljoin(url, image_url)
    
    data = {
        "product_page_url": product_page_url,
        "universal_product_code": universal_product_code,
        "title": title,
        "price_including_tax": price_including_tax,
        "price_excluding_tax": price_excluding_tax,
        "number_available": number_available,
        "product_description": product_description,
        "category": category,
        "review_rating": review_rating,
        "image_url": image_url,
    }
    
    if file_path:
        with open(file_path, "a", encoding='utf-8', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(data.values())
    
    return data