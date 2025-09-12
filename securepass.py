from hashlib import sha256
from os import urandom
import base64
from psycopg2 import Binary
from cryptography.fernet import Fernet

KEY = 'Rk1Jb2d6a1pZVzRrY0dBMFV5U3p6Zz09' # THIS IS HORRIBLE PRACTICE and only for demo! Better code shown in comment below:
# KEY = Fernet.generate_key() # Generates a secure, random 32-bit key to be stored securely

def hash_password(password):
    salt_bytes = urandom(16)
    salt_hex = salt_bytes.hex()
    pass_hash =  sha256(salt_bytes + password.encode('utf-8'))
    return salt_hex, pass_hash.hexdigest()

def encrypt_password(password):
    b64_key = base64.b64encode(KEY.encode())
    cipher = Fernet(b64_key)
    return Binary(cipher.encrypt(password.encode()))

def decrypt_password(password_bytes, key):
    b64_key = base64.b64encode(key.encode())
    cipher = Fernet(b64_key)
    encrypted_bytes = bytes(password_bytes)
    decrypted = cipher.decrypt(encrypted_bytes).decode()
    return decrypted

def hash_check(salt_hex, pass_hash, password):
    joined_bytes = bytes.fromhex(salt_hex) + password.encode('utf-8')
    return sha256(joined_bytes).hexdigest() == pass_hash