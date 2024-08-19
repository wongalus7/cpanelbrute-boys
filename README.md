# cPanel Brute Boys

![Screenshot](https://i.imgur.com/NqEbhZ1.png)
**cPanel Brute Crack Boys** dibuat menggunakan Python untuk melakukan brute-force attack pada login cPanel. Tools ini mendukung dua mode: single username dan mass username, memungkinkan pengguna untuk menguji banyak kombinasi username dan password secara efisien.

## Fitur

- **Dua Mode**: Pilih antara single username atau mass username untuk serangan brute-force.
- **Penanganan SSL**: Menonaktifkan peringatan SSL untuk menghubungkan ke host dengan HTTPS yang mungkin tidak memiliki sertifikat yang diverifikasi.

## Cara Penggunaan

Untuk menggunakan skrip ini, pastikan Anda telah menginstal dependencies yang diperlukan. Jika belum, Anda dapat menginstalnya menggunakan command ini di terminal:

```bash
apt install git
apt install python3
apt install python3-pip
pip3 install requests urllib3 colorama
git clone https://github.com/wongalus7/cpanelbrute-boys
cd cpanelbrute-boys
python3 cpanelbrute.py
```

## Disclaimer
Penggunaan skrip ini mungkin ilegal di beberapa yurisdiksi dan hanya boleh digunakan pada server yang Anda miliki atau telah diberi izin eksplisit untuk diuji. Penyalahgunaan alat ini dapat menyebabkan konsekuensi hukum yang serius. Pengguna bertanggung jawab untuk memastikan bahwa penggunaan mereka dari alat ini sepenuhnya sesuai dengan hukum dan peraturan lokal.
