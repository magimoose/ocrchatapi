from contextlib import asynccontextmanager
from fastapi import FastAPI, File, UploadFile, HTTPException, Form, Response
from services import ocr_file, chunk_by_paragraph, store_chunks, store_file
from dotenv import load_dotenv
import os
from supabase import Client, create_client, AuthApiError
from schemas import LoginRequest
from fastapi.responses import JSONResponse

load_dotenv()
supabase_url = os.getenv('SUPABASE_URL')
supabase_api_key = os.getenv('SUPABASE_API_KEY')

supabase: Client = create_client(supabase_url, supabase_api_key)


app = FastAPI()

@app.get('/')
def index():
    return {'message': 'OCR Chat API'}

@app.get('/document_ids')
async def document_ids():
    pass

@app.get('/documents')
async def documents():
    pass

@app.post('/login')
async def login(request: LoginRequest, response: Response):
    try: 
        result = supabase.auth.sign_in_with_password(
            {
                "email": request.email,
                "password": request.password
            }
        )

        access_token = result.session.access_token
        refresh_token = result.session.refresh_token

        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=True,
            samesite="Lax",
            path="/refresh"
        )

        return JSONResponse(
            content={"access_token": access_token},
            status_code=200
        )
    

    except AuthApiError as e:
        raise HTTPException(status_code=401, detail="Invalid email or password")

@app.post('/refresh')
async def refresh():
    pass

@app.post('/upload')
async def upload(
    file: UploadFile = File(...), 
    user_id: str = Form(...)
):
    content = await file.read()
    path = os.path.join(user_id, file.filename)
    output_path = store_file(content, file.content_type, supabase, path) # can use this to raise exception

    # content_json = ocr_file(content)
    # chunked_content = chunk_by_paragraph(content_json)
    # store_chunks(chunked_content, file.filename, file_id, supabase)

    return {"filename": file.filename, "status": "uploaded"}
    

@app.post('/query')
def query():
    pass

