from cryptography.fernet import Fernet

def load_key():
    return open("key.txt", "rb").read()

def encrypt_data(data):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt_data(token):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()
