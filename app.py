from flask import Flask, render_template
import json
import os

# 1. ANALISIS MASALAH: Konfigurasi Dasar
# Inisialisasi aplikasi Flask.
app = Flask(__name__)
# Menentukan path absolut ke direktori 'data'.
DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
JSON_FILE_PATH = os.path.join(DATA_DIR, 'data.json')

# 2. IDENTIFIKASI ASUMSI: Fungsi Pemuatan Data (Fokus JSON)
def load_json_data(file_path):
    """Membaca file JSON lokal dan mengembalikannya sebagai Python list/dict."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"ERROR: File JSON tidak ditemukan di: {file_path}")
        # Mengembalikan data kosong untuk menghindari error fatal di frontend
        return []
    except json.JSONDecodeError:
        print(f"ERROR: Gagal mendekode JSON di: {file_path}")
        return []

# 3. KAJI ALTERNATIF: Route Utama
@app.route('/')
def index():
    """Route utama yang memuat data JSON dan menampilkannya di frontend."""
    # Load data
    data_list = load_json_data(JSON_FILE_PATH)
    
    # Memeriksa data dan mengekstrak kunci (key/element) untuk header tabel
    if data_list and isinstance(data_list, list) and data_list[0]:
        # Mengambil semua kunci dari item pertama (asumsi data konsisten)
        keys = list(data_list[0].keys()) 
    else:
        # Menangani kasus jika data kosong atau tidak valid
        keys = ["Data Tidak Ditemukan atau Format Salah"]
    
    # 4. KESIMPULAN LOGIS: Render Template
    # Meneruskan data (data_list) dan kunci (keys) ke template Jinja
    return render_template(
        'index.html', 
        title='Data Produk dari JSON', 
        data=data_list, 
        keys=keys
    )

# 5. (OPSIONAL) INSIGHT TAMBAHAN: Route Tambahan
# Contoh route tambahan untuk membuktikan kemampuan multi-format
@app.route('/about')
def about():
    # Ini route statis, tidak memuat data, hanya sebagai contoh ekstensi
    return "Halaman ini menunjukkan bahwa backend berfungsi."

# Menjalankan aplikasi
if __name__ == '__main__':
    # Pastikan direktori 'data' ada
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"Direktori 'data' dibuat di: {DATA_DIR}")
    
    # Start server
    app.run(debug=True)