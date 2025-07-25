# generate_vector_store.py

from pdf_reader import load_pdf_text, split_text
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import os

# Load the embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_store(chunks: list, save_path: str = "faiss_index") -> FAISS:
    """Creates and saves a FAISS index from the provided text chunks"""
    documents = [Document(page_content=chunk) for chunk in chunks]
    db = FAISS.from_documents(documents, embedding_model)
    db.save_local(save_path)
    return db

def load_vector_store(save_path: str = "faiss_index") -> FAISS:
    """Loads the FAISS index from disk"""
    return FAISS.load_local(save_path, embedding_model)

# ---- MAIN PIPELINE ----
if __name__ == "__main__":
    pdf_path = "pdf1.pdf"  # Replace with your actual PDF name
    text = load_pdf_text(pdf_path)
    chunks = split_text(text)
    create_vector_store(chunks)
    print("✅ Vector store created and saved.")
