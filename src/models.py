from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID, JSON
from pydantic import BaseModel

class Documents(Base):
    __tablename__ = 'documents'

    doc_id = Column(Integer, primary_key=True, index=True)
    doc_name = Column(String, index=True)
    doc_content = Column(String)
    metadata = Column(JSON)

class Document_Chunk(Base):
    __tablename__ = 'document_chunk'

    chunk_id = Column(Integer, primary_key=True, index=True)
    doc_id = Column(String, ForeignKey("documents.doc_id"), index=True)
    doc_name = Column(String, index=True)
    chunk_content = Column(String)
    chunk_metadata = Column(JSON)