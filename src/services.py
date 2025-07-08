from supabase import Client
from fastapi import UploadFile
import uuid

def ocr_file(content: bytes):
    pass

def chunk_by_paragraph():
    pass

def store_file(content: bytes, content_type: str, supabase: Client, input_path: str):
    output_path, _ = supabase.storage.from_("documents").upload(
        path=input_path,
        file=content,
        file_options={"content-type": content_type}
    )
    return output_path
    

def store_chunks(content: str, filename: str, client: Client):
    pass