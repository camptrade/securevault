import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()  # .env faylındakı açarları oxuyur

BUCKET = "vault"


def get_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise RuntimeError(".env faylında SUPABASE_URL və SUPABASE_KEY yoxdur")
    return create_client(url, key)


def upload_bytes(name: str, data: bytes) -> None:
    """Şifrəli məlumatı buluda yükləyir."""
    get_client().storage.from_(BUCKET).upload(
        name, data, {"content-type": "application/octet-stream", "upsert": "true"}
    )


def download_bytes(name: str) -> bytes:
    """Buluddan faylı endirir."""
    return get_client().storage.from_(BUCKET).download(name)