import requests
import logging
import pandas as pd
from bs4 import BeautifulSoup

def scrape_data(url: str) -> list:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise Exception(f"Gagal mengakses {url}: {err}")
    
    try:
        soup = BeautifulSoup(response.text, "html.parser")
        product = []
        cards = soup.find_all("div", class_="collection-card")
        for card in cards:
            title = card.select_one('.product-title').text.strip()
            price = card.select_one('.product-price').text.strip().replace("$", "")
            rating = card.select_one('.product-rating').text.strip().replace(" / 5", "")
            colors = card.select_one('.product-colors').text.strip().replace(" Colors", "")
            size = card.select_one('.product-size').text.strip().replace("Size: ", "")
            gender = card.select_one(".product-gender").text.strip().replace("Gender: ", "")
            product.append({
                    'title': title,
                    'price': price,
                    'rating': rating,
                    'colors': colors,
                    'size': size,
                    'gender': gender                                 
            })

    except Exception as e:
        print(f"Error: {e}")
        return []

    return product
    
    