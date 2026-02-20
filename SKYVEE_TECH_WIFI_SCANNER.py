import subprocess
import socket
import os
import sys
import time
import csv
from datetime import datetime

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    print("Install colorama dulu: pip install colorama")
    sys.exit(1)

# ==============================
#  COLORS
# ==============================
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
B = Fore.BLUE
M = Fore.MAGENTA
RESET = Style.RESET_ALL

# ==============================
#  HEADER
# ==============================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    clear()
    print(G + """
  ================================================================
   __          ___ ______ _____    _____  _____          _   _ 
   \ \        / (_)  ____|_   _|  / ____|/ ____|   /\   | \ | |
    \ \  /\  / / _| |__    | |   | (___ | |       /  \  |  \| |
     \ \/  \/ / | |  __|   | |    \___ \| |      / /\ \ | . ` |
      \  /\  /  | | |     _| |_   ____) | |____ / ____ \| |\  |
       \/  \/   |_|_|    |_____| |_____/ \_____/_/    \_\_| \_|
  
          W I F I   S C A N N E R   v 1 . 0
               by  S K Y V E E  T E C H
  ================================================================
    """ + RESET)

# ==============================
#  SCAN WIFI TERSIMPAN + PASSWORD
# ==============================
def scan_saved_wifi():
    header()
    print(G + "  [*] Scanning saved WiFi profiles...\n" + RESET)
    
    try:
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'profiles'],
            capture_output=True, text=True
        )
        profiles = [
            line.split(":")[1].strip()
            for line in result.stdout.split('\n')
            if "All User Profile" in line
        ]

        if not profiles:
            print(R + "  [-] Tidak ada WiFi tersimpan." + RESET)
            input("\n  Tekan Enter untuk kembali...")
            return

        count = 0
        for ssid in profiles:
            count += 1
            try:
                detail = subprocess.run(
                    ['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'],
                    capture_output=True, text=True
                )
                password = "No Password / Not Found"
                auth = "Unknown"
                for line in detail.stdout.split('\n'):
                    if "Key Content" in line:
                        password = line.split(":")[1].strip()
                    if "Authentication" in line:
                        auth = line.split(":")[1].strip()

                print(G + f"  [{count}] SSID        : " + C + ssid)
                print(G + f"      Password    : " + Y + password)
                print(G + f"      Auth        : " + W + auth)
                print(G + "  " + "-"*58 + RESET)

            except Exception:
                pass

        print(G + f"\n  [*] Total WiFi found: {count}" + RESET)

    except Exception as e:
        print(R + f"  [-] Error: {e}" + RESET)

    input("\n  Tekan Enter untuk kembali...")

# ==============================
#  SCAN DEVICE DI JARINGAN
# ==============================
def scan_network_devices():
    header()
    print(G + "  [*] Scanning devices in local network...\n" + RESET)

    try:
        # Dapatkan IP lokal
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        ip_base = ".".join(local_ip.split(".")[:3])

        print(C + f"  [*] Your IP     : {local_ip}")
        print(C + f"  [*] Scanning    : {ip_base}.1 - {ip_base}.254")
        print(C + f"  [*] Please wait...\n" + RESET)

        active = []
        for i in range(1, 255):
            ip = f"{ip_base}.{i}"
            result = subprocess.run(
                ['ping', '-n', '1', '-w', '200', ip],
                capture_output=True, text=True
            )
            if "TTL=" in result.stdout:
                try:
                    hostname_result = socket.gethostbyaddr(ip)
                    name = hostname_result[0]
                except:
                    name = "Unknown"
                active.append((ip, name))
                print(G + f"  [+] {ip:<18} | {name}" + RESET)

        print(G + f"\n  [*] Total devices found: {len(active)}" + RESET)

    except Exception as e:
        print(R + f"  [-] Error: {e}" + RESET)

    input("\n  Tekan Enter untuk kembali...")

# ==============================
#  CEK INFO JARINGAN AKTIF
# ==============================
def network_info():
    header()
    print(G + "  [*] Network Information\n" + RESET)

    try:
        result = subprocess.run(
            ['ipconfig', '/all'],
            capture_output=True, text=True
        )
        lines = result.stdout.split('\n')
        for line in lines:
            if any(k in line for k in [
                "IPv4", "IPv6", "Default Gateway",
                "DNS Servers", "Physical Address",
                "DHCP Server", "Subnet Mask", "Wi-Fi", "Ethernet"
            ]):
                line = line.strip()
                if line:
                    if "Wi-Fi" in line or "Ethernet" in line:
                        print(M + f"\n  {line}" + RESET)
                    else:
                        key, _, val = line.partition(":")
                        print(G + f"  {key.strip():<25} : " + C + val.strip() + RESET)

    except Exception as e:
        print(R + f"  [-] Error: {e}" + RESET)

    input("\n  Tekan Enter untuk kembali...")

# ==============================
#  EXPORT HASIL KE CSV
# ==============================
def export_wifi_csv():
    header()
    print(G + "  [*] Exporting saved WiFi to CSV...\n" + RESET)

    try:
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'profiles'],
            capture_output=True, text=True
        )
        profiles = [
            line.split(":")[1].strip()
            for line in result.stdout.split('\n')
            if "All User Profile" in line
        ]

        filename = f"wifi_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["No", "SSID", "Password", "Authentication"])

            count = 0
            for ssid in profiles:
                count += 1
                try:
                    detail = subprocess.run(
                        ['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'],
                        capture_output=True, text=True
                    )
                    password = "No Password"
                    auth = "Unknown"
                    for line in detail.stdout.split('\n'):
                        if "Key Content" in line:
                            password = line.split(":")[1].strip()
                        if "Authentication" in line:
                            auth = line.split(":")[1].strip()
                    writer.writerow([count, ssid, password, auth])
                except:
                    pass

        print(G + f"  [+] Exported {count} WiFi profiles!" + RESET)
        print(G + f"  [+] File saved as: {filename}" + RESET)

    except Exception as e:
        print(R + f"  [-] Error: {e}" + RESET)

    input("\n  Tekan Enter untuk kembali...")

# ==============================
#  MENU UTAMA
# ==============================
def menu():
    while True:
        header()
        print(W + "  [1]  Scan Saved WiFi + Passwords")
        print(W + "  [2]  Scan Devices in Network")
        print(W + "  [3]  Network Info")
        print(W + "  [4]  Export WiFi to CSV")
        print(W + "  [0]  Exit")
        print(G + "\n  ================================================================" + RESET)

        choice = input(G + "\n  [?] Choose: " + RESET).strip()

        if choice == "1":
            scan_saved_wifi()
        elif choice == "2":
            scan_network_devices()
        elif choice == "3":
            network_info()
        elif choice == "4":
            export_wifi_csv()
        elif choice == "0":
            clear()
            print(G + """
  ================================================================
   Thanks for using SKYVEE TECH - WiFi Scanner
   github.com/Skyvee-Tech
  ================================================================
            """ + RESET)
            time.sleep(2)
            sys.exit(0)
        else:
            pass

# ==============================
#  MAIN
# ==============================
if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(R + "\n\n  [!] Interrupted by user." + RESET)
        sys.exit(0)
