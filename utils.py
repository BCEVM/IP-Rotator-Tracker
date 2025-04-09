import requests
import uuid

def get_current_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return ip
    except:
        return "Unavailable"

def get_real_info():
    try:
        data = requests.get("https://ipinfo.io/json").json()
        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "org": data.get("org"),
            "mac": get_mac()
        }
    except:
        return {"ip": "?", "mac": get_mac()}

def get_mac():
    return ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                     for ele in range(0, 8*6, 8)][::-1])

def save_ip_log(data):
    with open("ip_log.txt", "a") as f:
        f.write(data + "\n")
