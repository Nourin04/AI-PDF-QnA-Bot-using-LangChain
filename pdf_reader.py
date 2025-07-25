from PyPDF2 import PdfReader
from typing import List
import re

def load_pdf_text(pdf_path: str) -> str:
    """Extract all text from a PDF file"""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def split_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Split long text into smaller overlapping chunks"""
    sentences = re.split(r'(?<=[.?!])\s+', text)
    
    chunks = []
    chunk = ""
    for sentence in sentences:
        if len(chunk) + len(sentence) <= chunk_size:
            chunk += sentence + " "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + " "
    
    if chunk:
        chunks.append(chunk.strip())
    
    # Add overlap
    final_chunks = []
    for i in range(0, len(chunks), max(1, chunk_size - overlap)):
        final_chunks.append(" ".join(chunks[i:i+3]))
        
    return final_chunks
