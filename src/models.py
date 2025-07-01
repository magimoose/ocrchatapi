from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID, JSON
from database import Base

class Documents(Base):
    __tablename__ = 'documents'

    doc_id = Column(Integer, primary_key=True, index=True)
    doc_name = Column(String, index=True)
    doc_content = Column(String)
    metadata = Column(JSON)

class Document_Chunk(Base);
    __tablename__ = 'document_chunk'

    chunk_id = Column(Integer, primary_key=True, index=True)
    