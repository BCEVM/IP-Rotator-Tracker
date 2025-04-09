from ip_rotator import rotate_ip
from webhook_manager import send_webhook_notification
from utils import get_current_ip, save_ip_log
from encryptor import encrypt_data
import time

ROTATE_INTERVAL = 30  # Detik
LOG_EVERY = 5  # Kirim notifikasi tiap 5 rotasi

def main():
    count = 0
    while True:
        rotate_ip()
        current_ip = get_current_ip()
        log_entry = f"[+] Current IP: {current_ip}"
        print(log_entry)
        encrypted = encrypt_data(log_entry)
        save_ip_log(encrypted)

        count += 1
        if count % LOG_EVERY == 0:
            send_webhook_notification(current_ip)

        time.sleep(ROTATE_INTERVAL)

if __name__ == "__main__":
    main()
