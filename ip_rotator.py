from stem import Signal
from stem.control import Controller

def rotate_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password="passwordtorlo")  # Ganti sesuai torrc
            controller.signal(Signal.NEWNYM)
    except Exception as e:
        print(f"[!] Gagal rotate IP: {e}")
