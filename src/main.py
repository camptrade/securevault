import sys
import os
import getpass

sys.path.insert(0, os.path.dirname(__file__))
from crypto_utils import encrypt_file, decrypt_file, sha256_hash


def fayl_hash(yol):
    with open(yol, "rb") as f:
        return sha256_hash(f.read())


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("encrypt", "decrypt"):
        print("İstifadə:")
        print("  python src/main.py encrypt demo/gizli.txt")
        print("  python src/main.py decrypt demo/gizli.txt.enc")
        return

    emr, yol = sys.argv[1], sys.argv[2]
    parol = getpass.getpass("Parol: ")

    if emr == "encrypt":
        cixis = yol + ".enc"
        print("SHA-256 (şifrələmədən əvvəl):", fayl_hash(yol))
        encrypt_file(yol, cixis, parol)
        print("Şifrələndi ->", cixis)
    else:
        qovluq = os.path.dirname(yol)
        ad = os.path.basename(yol).removesuffix(".enc")
        cixis = os.path.join(qovluq, "acilmis_" + ad)
        try:
            decrypt_file(yol, cixis, parol)
        except Exception:
            print("XƏTA: parol səhvdir və ya fayl dəyişdirilib!")
            return
        print("Açıldı ->", cixis)
        print("SHA-256 (açıldıqdan sonra):", fayl_hash(cixis))


main()