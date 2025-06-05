import pandas as pd

def cleaned_price(price):
    try:
        return float(price.replace("$", "")) * 16000
    except Exception as e:
        print(f"Error converting price: {price} - {e}")
        return None
    
def cleaned_rating(rating):
    try:
        if isinstance(rating, str) and "/" in rating:
            return float(rating.split("/")[0].strip())
        return float(rating)
    except Exception as e:
        print(f"Error converting rating: {rating} - {e}")
        return None

def cleaned_colors(colors):
    try:
        return int(str(colors).split()[0])
    except Exception as e:
        print(f"Error converting colors: {colors} - {e}")
    return None

def cleaned_size(size):
    try:
        return str(size).replace("Size: ", "").strip()
    except Exception as e:
        print(f"Error cleaning size: {size} - {e}")
    return None

def cleaned_gender(gender):
    try:
        return str(gender).replace("Gender: ", "").strip()
    except Exception as e:
        print(f"Error cleaning gender: {gender} - {e}")
    return None

def transform_data(df): 
    try: 
        df = df[~df["title"].astype(str).str.contains(".jpeg", na=False)]
        df = df[df["title"].str.lower() != "Produk tidak ditemukan."]

        df["price"] = df["price"].apply(cleaned_price)
        df["rating"] = df["rating"].apply(cleaned_rating)
        df["colors"] = df["colors"].apply(cleaned_colors)
        df["size"] = df["size"].apply(cleaned_size)
        df["gender"] = df["gender"].apply(cleaned_gender)

        df = df.drop_duplicates()
        df = df.dropna()

    except Exception as e:
        raise Exception(f"An error occurred during data transformation: {e}") from e