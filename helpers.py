import os

import requests


def clean_text(text: str) -> str:
    """Clean text by removing extra whitespace and newlines"""
    return ' '.join(text.strip().split())



def download_image(url: str):
    """Download image from url"""
    
    folder_path = "assets/images"
    os.makedirs(folder_path, exist_ok=True)
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_path, os.path.basename(url)), "wb") as f:
            f.write(response.content)
            
    return True
