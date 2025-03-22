import csv


from scrape_book_website import scrape_all_categories


def main():
    """Main function"""
    url = "https://books.toscrape.com/index.html"
    
    file_path = "assets/books_data.csv"
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
    
    print("Scrapin Start \n")
    
    with open(file_path, "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(headers)
        

    res = scrape_all_categories(url, file_path)
    
    print("Scrapin End \n")
    return 1


if __name__ == "__main__":
    main()
