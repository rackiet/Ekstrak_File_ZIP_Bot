import os
import zipfile

# Lokasi folder yang berisi file zip
folder_path = "Go Ekstrak"

# Dapatkan daftar semua file dan folder di dalam folder_path
daftar_file = os.listdir(folder_path)

# Iterasi melalui setiap item di dalam folder_path
for item in daftar_file:
    item_path = os.path.join(folder_path, item)
    
    # Cek apakah item adalah file dan apakah itu adalah file zip
    if os.path.isfile(item_path) and zipfile.is_zipfile(item_path):
        # Buat folder baru dengan nama file zip (tanpa ekstensi)
        new_folder = os.path.join(folder_path, os.path.splitext(item)[0])
        os.makedirs(new_folder, exist_ok=True)
        
        # Buka file zip
        with zipfile.ZipFile(item_path, 'r') as zip_ref:
            # Ekstrak semua konten zip ke folder baru
            zip_ref.extractall(new_folder)

        print(f"File {item} telah diekstrak ke folder {new_folder}")

print("Proses ekstraksi selesai.")
