import os
import zipfile

def extract_zip_files(directory):
    # Jelajahi semua file di direktori yang diberikan
    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            # Buat nama folder berdasarkan nama file zip (tanpa ekstensi .zip)
            folder_name = os.path.splitext(filename)[0]
            folder_path = os.path.join(directory, folder_name)
            
            # Membuat folder jika belum ada
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Mengekstrak file zip ke dalam folder tersebut
            zip_file_path = os.path.join(directory, filename)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
            print(f"File '{filename}' telah diekstrak ke folder '{folder_name}'")

if __name__ == "__main__":
    dir_path = input("Masukkan nama folder yang berisi file zip: ")
    extract_zip_files(dir_path)
