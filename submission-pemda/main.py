from utils.extract import ambil_data
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_gsheet, load_to_postgres

BASE_URL = 'https://fashion-studio.dicoding.dev/'
MAX_PAGES = 50

def main():
    all_products = []

    print(f"Mengambil data: {BASE_URL}")
    try:
        produk = ambil_data(BASE_URL)
        all_products.extend(produk)
    except Exception as e:
        print(f"❌ Gagal mengambil data: {e}")

    for pages in range(1, MAX_PAGES):
        url_halaman = f"{BASE_URL}page{pages}"
        print(f"Mengambil data halaman {pages}: {url_halaman}")
        try:
            produk = ambil_data(url_halaman)
            all_products.extend(produk)
        except Exception as e:
            print(f"❌ Gagal mengambil data halaman {pages}: {e}")

    if not all_products:
        print("❌ Tidak ada produk yang berhasil diambil. Program dihentikan.")
        return None
    
    data_bersih = transform_data(all_products)

    load_to_csv(data_bersih)
    load_to_gsheet(data_bersih, sheet_id='18b0lPQMZl-d-8__NXWj6ZhsEOz8VHCLZzB9r1RgFHJ8', nama_worksheet="Sheet1")
    load_to_postgres(data_bersih, nama_tabel='products')

    print("✅ Semua proses ETL selesai.")

if __name__ == "__main__":
    main()