import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from crypto_utils import encrypt, decrypt, sha256_hash

mesaj = "Bu gizli məlumatdır".encode()

# Test 1: şifrələ və aç
sifreli = encrypt(mesaj, "parol123")
assert decrypt(sifreli, "parol123") == mesaj
print("Test 1 keçdi: şifrələmə və açma işləyir")

# Test 2: səhv parol
try:
    decrypt(sifreli, "sehv_parol")
    print("Test 2 UĞURSUZ")
except Exception:
    print("Test 2 keçdi: səhv parol ilə açmaq olmur")

# Test 3: fayl dəyişdirilib
bozuq = bytearray(sifreli)
bozuq[-1] ^= 1
try:
    decrypt(bytes(bozuq), "parol123")
    print("Test 3 UĞURSUZ")
except Exception:
    print("Test 3 keçdi: dəyişdirilmiş fayl aşkar olundu")

# Test 4: eyni mesaj hər dəfə fərqli şifrələnir
assert encrypt(mesaj, "parol123") != encrypt(mesaj, "parol123")
print("Test 4 keçdi: hər şifrələmə fərqlidir (salt və nonce)")

# Test 5: SHA-256
print("SHA-256:", sha256_hash(mesaj))