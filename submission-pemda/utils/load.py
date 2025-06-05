import pandas as pd
import os
import datetime
from sqlalchemy import create_engine

def load_to_csv(df, nama_file="products.csv"):
    try: 
        os.makedirs(os.path.dirname(nama_file), exist_ok=True)
        df.to_csv(nama_file, index=False)
        print(f"✅ Data berhasil disimpan ke {nama_file}")
    except Exception as e:
        print(f"Gagal menyimpan ke CSV: {e}")
    
def load_to_gsheet(df, sheet_id, nama_worksheet="Sheet1"):
    try:
        import gspread
        from gspread_dataframe import set_with_dataframe
        from oauth2client.service_account import ServiceAccountCredentials

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('key_api.json', scopes=scope)
        client = gspread.authorize(creds)

        spreadsheet = client.open_by_key(sheet_id)
        worksheet = spreadsheet.worksheet(nama_worksheet)

        worksheet.clear()
        set_with_dataframe(worksheet, df)

        print(f"[{datetime.datetime.now()}] ✅ Data berhasil disimpan ke Google Sheets: {nama_worksheet}")
    except FileNotFoundError:
        print(f"[{datetime.datetime.now()}] ❌ File kredensial Google Sheets tidak ditemukan.")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] ❌ Gagal menyimpan ke Google Sheets: {e}")

def load_to_postgres(df, nama_tabel='products'):
    try:
        username = 'postgres'
        password = 'selesaikan1'
        host = 'localhost'
        port = '5432'
        database = 'product_db'

        engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

        df.to_sql(nama_tabel, engine, if_exists='replace', index=False)
        print(f"[{datetime.datetime.now()}] ✅ Data berhasil disimpan ke tabel PostgreSQL '{nama_tabel}'.")

    except Exception as e:
        print(f"[{datetime.datetime.now()}] ❌Gagal menyimpan data ke PostgreSQL: {e}")