from contextlib import asynccontextmanager
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from services import ocr_file, chunk_by_paragraph, store_chunks, store_file


app = FastAPI()

@asynccontextmanager
def init_database

@app.get('/')
def index():
    return {'message': 'OCR Chat API'}

@app.get('/document_ids')
async def document_ids():
    pass

@app.get('/documents')
async def documents():
    pass

@app.post('/upload')
async def upload(
    file: UploadFile = File(...), 
    file_id: str = Form(...),
    user_id: str = Form(...)
):
    content = await file.read()
    content_json = ocr_file(content)
    chunked_content = chunk_by_paragraph(content_json)
    store_chunks(chunked_content, filename)
    store_file(content, filename)
    return {"filename": filename, "status": "uploaded"}
    

@app.post('/query')
def query():
    pass

