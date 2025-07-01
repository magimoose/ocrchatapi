from pydantic import BaseModel

class DocumentMetadata(BaseModel):
    doc_id: str
    filename: str
    #description: str #may be unneccesary

class ChunkMetadata:
    chunk_id: str
    filename: str
    page_nmr: int
    polygon: list[int]