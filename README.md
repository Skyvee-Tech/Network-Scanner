<h1 align="center">📡 Network Scanner </h1>
<h3 align="center">// scan, detect, and export. powered by python.</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows-blue?style=flat-square&logo=windows" />
  <img src="https://img.shields.io/badge/Language-Python-green?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Version-1.0-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/Made%20by-Skyvee Tech-red?style=flat-square" />
</p>

---

## 📌 About

Terminal-based WiFi Scanner tool by **SKYVEE TECH** — versi Python yang lebih powerful dari WiFi Viewer sebelumnya.

Tidak hanya lihat password WiFi tersimpan, tool ini juga bisa **scan semua device di jaringan**, lihat info jaringan lengkap, dan export hasilnya ke CSV.

---

## ⚡ Features

| Menu | Fitur |
|------|-------|
| `[1]` | Scan semua WiFi tersimpan + password + authentication type |
| `[2]` | Scan semua device aktif di jaringan lokal + hostname |
| `[3]` | Lihat info jaringan lengkap (IP, DNS, Gateway, MAC Address) |
| `[4]` | Export semua WiFi tersimpan ke file `.csv` |
| `[0]` | Exit |

---

## 🚀 How to Use (User)

### Menggunakan .exe (Direkomendasikan)

1. Download `SKYVEE_TECH_WIFI_SCANNER.exe` dari halaman **Releases**
2. Klik kanan → **Run as Administrator**
3. Pilih menu yang diinginkan
4. Done!

> ⚠️ **Wajib Run as Administrator** — tanpa ini password WiFi dan scan jaringan tidak akan berjalan.

> ⚠️ **Windows Defender / Antivirus** mungkin mendeteksi file `.exe` sebagai ancaman. Ini adalah **False Positive** karena file dibuat menggunakan PyInstaller. Kode sumber tersedia untuk diperiksa di repo ini.

---

## 🛠️ Developer Guide

Panduan ini untuk kamu yang ingin menjalankan, memodifikasi, atau berkontribusi pada source code.

### Requirements

- Python 3.8 atau lebih baru
- pip (sudah termasuk di Python 3.4+)
- Windows 10 / 11

### 1. Clone Repository

```bash
git clone https://github.com/Skyvee-Tech/Network-Scanner.git
cd Network-Scanner
```

### 2. Install Dependencies

```bash
pip install colorama scapy
```

### 3. Jalankan Script

```bash
python SKYVEE_TECH_WIFI_SCANNER.py
```

> Jalankan CMD atau Terminal sebagai **Administrator** sebelum menjalankan script.

### 4. Build ke .exe (Opsional)

Kalau kamu mau build ulang jadi `.exe`, install PyInstaller dulu:

```bash
pip install pyinstaller
```

Lalu build:

```bash
pyinstaller --onefile SKYVEE_TECH_WIFI_SCANNER.py
```

File `.exe` akan tersimpan di folder `dist/`.

### Struktur File

```
📁 Network-Scanner
├── SKYVEE_TECH_WIFI_SCANNER.py   <- source code utama
├── SKYVEE_TECH_WIFI_SCANNER.exe  <- executable (sudah di-build)
├── README.md                     <- dokumentasi
└── LICENSE                       <- lisensi MIT
```

### Dependencies

| Library | Fungsi | Install |
|---------|--------|---------|
| `colorama` | Tampilan berwarna di terminal | `pip install colorama` |
| `scapy` | Network scanning | `pip install scapy` |
| `subprocess` | Jalankan command Windows | Built-in Python |
| `socket` | Deteksi hostname device | Built-in Python |
| `csv` | Export hasil ke spreadsheet | Built-in Python |

---

## 📋 Output Example

### Scan Saved WiFi
```
  [1] SSID        : MyHomeWifi
      Password    : mypassword123
      Auth        : WPA2-Personal
  ----------------------------------------------------------
  [*] Total WiFi found: 5
```

### Scan Devices in Network
```
  [*] Your IP     : 192.168.1.5
  [*] Scanning    : 192.168.1.1 - 192.168.1.254

  [+] 192.168.1.1        | router.local
  [+] 192.168.1.3        | DESKTOP-ABC123
  [+] 192.168.1.7        | Unknown

  [*] Total devices found: 3
```

### Export CSV
```
  [+] Exported 15 WiFi profiles!
  [+] File saved as: wifi_export_20260220_153000.csv
```

---

## ⚠️ Disclaimer

Tool ini dibuat untuk keperluan **edukasi dan penggunaan pribadi**.
Hanya gunakan pada jaringan milik sendiri atau yang sudah ada izinnya.
Developer tidak bertanggung jawab atas penyalahgunaan tool ini.

---

## 📜 License

MIT License — bebas dipakai, dimodifikasi, dan disebarkan.
Tetap cantumkan credit ya. 😎

---

<p align="center">Made with 💻 by <a href="https://github.com/Skyvee-Tech">Skyvee Tech</a></p>
