# 📡 SKYVEE TECH - WiFi Scanner Python version

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**SKYVEE TECH WiFi Scanner** adalah alat berbasis CLI (Command Line Interface) yang dirancang untuk membantu pengelolaan jaringan lokal pada sistem operasi Windows. Alat ini memungkinkan pengguna untuk melihat password WiFi yang tersimpan, memindai perangkat yang terhubung di jaringan, dan mengekspor data ke format CSV.

---

## 🚀 Fitur Utama

* **🔓 Scan Saved WiFi + Passwords**: Menampilkan daftar semua SSID WiFi yang pernah terhubung beserta kata sandinya.
* **🔍 Network Device Scanner**: Melakukan pemindaian IP aktif di jaringan lokal untuk melihat perangkat yang sedang terhubung.
* **📊 Network Information**: Menampilkan detail adapter jaringan (IP, MAC Address, DNS, dll) secara ringkas.
* **📂 Export to CSV**: Menyimpan daftar password WiFi yang tersimpan ke dalam file `.csv` untuk cadangan.
* **🎨 Colorized Interface**: Tampilan terminal yang berwarna dan mudah dibaca berkat library `colorama`.

---
## 📦 Versi Executable (.exe)
Untuk pengguna umum, Anda dapat langsung menjalankan file .exe tanpa perlu menginstal Python:

1. Unduh file SKYVEE_WiFi_Scanner.exe dari folder dist/ atau halaman Releases.
2. Klik kanan pada file tersebut dan pilih Run as Administrator.
   *Catatan: Hak akses Admin diperlukan agar sistem bisa membaca data password WiFi.
3. Jika muncul peringatan Windows Protected Your PC, klik More Info > Run Anyway.

## ⚠️ Catatan Keamanan & Privasi
- False Positive: File executable yang dibuat dengan PyInstaller seringkali dideteksi sebagai ancaman oleh antivirus (seperti Windows Defender) karena melakukan pemindaian jaringan. Ini adalah False Positive. Kode ini aman dan transparan.
- Etika: Gunakan alat ini hanya untuk keperluan edukasi atau mengelola jaringan milik pribadi.

## 🛠️ Cara Instalasi (Untuk Developer)

Jika Anda ingin menjalankan atau memodifikasi kode sumber (`.py`):

1. **Clone Repository**:
   ```bash
   git clone [https://github.com/Skyvee-Tech/WIFI-SCANNER.git](https://github.com/Skyvee-Tech/WIFI-SCANNER.git)
   cd WIFI-SCANNER
2. **Instal Library**:
  ```bash
   pip install colorama
