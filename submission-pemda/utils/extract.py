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
            try:
                name = card.select_one('.product-name').text.strip()
                price = card.select_one('.product-price').text.strip()
                rating = card.select_one('.product-rating').text.strip()
                image = card.select_one('img')['src']
                product.append({
                    'name': name,
                    'price': price,
                    'rating': rating,
                    'image_url': image
                })
            except Exception as e:
                logger.warning(f"Skipping a card: {e}")
        return data
    
    except Exception as e:
        print(f"Error: {e}")
        return []
