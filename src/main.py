import sys
import os
import getpass

sys.path.insert(0, os.path.dirname(__file__))
from crypto_utils import encrypt, decrypt, encrypt_file, decrypt_file, sha256_hash


def fayl_hash(yol):
    with open(yol, "rb") as f:
        return sha256_hash(f.read())


def main():
    emrler = ("encrypt", "decrypt", "upload", "download")
    if len(sys.argv) != 3 or sys.argv[1] not in emrler:
        print("İstifadə:")
        print("  python src/main.py encrypt demo/gizli.txt")
        print("  python src/main.py decrypt demo/gizli.txt.enc")
        print("  python src/main.py upload demo/gizli.txt")
        print("  python src/main.py download gizli.txt.enc")
        return

    emr, yol = sys.argv[1], sys.argv[2]
    parol = getpass.getpass("Parol: ")

    if emr == "encrypt":
        cixis = yol + ".enc"
        print("SHA-256 (şifrələmədən əvvəl):", fayl_hash(yol))
        encrypt_file(yol, cixis, parol)
        print("Şifrələndi ->", cixis)

    elif emr == "decrypt":
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

    elif emr == "upload":
        from cloud_utils import upload_bytes
        with open(yol, "rb") as f:
            data = f.read()
        print("SHA-256 (şifrələmədən əvvəl):", sha256_hash(data))
        blob = encrypt(data, parol)          # əvvəl kompüterdə şifrələ
        ad = os.path.basename(yol) + ".enc"
        upload_bytes(ad, blob)               # sonra buluda göndər
        print("Şifrələnib buluda yükləndi ->", ad)

    elif emr == "download":
        from cloud_utils import download_bytes
        blob = download_bytes(yol)
        try:
            data = decrypt(blob, parol)
        except Exception:
            print("XƏTA: parol səhvdir və ya fayl dəyişdirilib!")
            return
        cixis = os.path.join("demo", "buluddan_" + yol.removesuffix(".enc"))
        with open(cixis, "wb") as f:
            f.write(data)
        print("Buluddan endirildi və açıldı ->", cixis)
        print("SHA-256 (açıldıqdan sonra):", sha256_hash(data))


main()