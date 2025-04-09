# IP-Rotator-Tracker

Auto IP changer menggunakan Tor. 
Dilengkapi enkripsi log dan notifikasi ntfy.sh.

## Fitur:
- Auto rotasi IP via Tor
- Tracking IP & MAC address asli
- Deteksi VPN/Proxy
- Enkripsi data tracking (AES-256)
- Notifikasi via ntfy.sh
- Modular & open for extension

## Setup:
1. Jalankan Tor service (`tor` & `tor --hash-password yourpassword`)
2. Simpan hash ke `torrc`, aktifkan port 9051
3. Generate key: `openssl rand -base64 32 > key.txt`
4. Install dependen:
```bash
pip install requests cryptography stem pysocks
