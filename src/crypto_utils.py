import os
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


def derive_key(password: str, salt: bytes) -> bytes:
    """Paroldan 32 baytlıq (256 bit) açar düzəldir."""
    kdf = Scrypt(salt=salt, length=32, n=2**15, r=8, p=1)
    return kdf.derive(password.encode())


def encrypt(data: bytes, password: str) -> bytes:
    """Məlumatı şifrələyir."""
    salt = os.urandom(16)    # təsadüfi "duz"
    nonce = os.urandom(12)   # təsadüfi birdəfəlik nömrə
    key = derive_key(password, salt)
    ciphertext = AESGCM(key).encrypt(nonce, data, None)
    return salt + nonce + ciphertext


def decrypt(blob: bytes, password: str) -> bytes:
    """Şifrəli məlumatı açır. Parol səhvdirsə və ya fayl dəyişdirilibsə, xəta verir."""
    salt = blob[:16]
    nonce = blob[16:28]
    ciphertext = blob[28:]
    key = derive_key(password, salt)
    return AESGCM(key).decrypt(nonce, ciphertext, None)


def sha256_hash(data: bytes) -> str:
    """Məlumatın SHA-256 "barmaq izini" qaytarır."""
    return hashlib.sha256(data).hexdigest()


def encrypt_file(input_path: str, output_path: str, password: str) -> None:
    with open(input_path, "rb") as f:
        data = f.read()
    with open(output_path, "wb") as f:
        f.write(encrypt(data, password))


def decrypt_file(input_path: str, output_path: str, password: str) -> None:
    with open(input_path, "rb") as f:
        blob = f.read()
    with open(output_path, "wb") as f:
        f.write(decrypt(blob, password))