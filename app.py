import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from tempfile import NamedTemporaryFile
from dotenv import load_dotenv
import os

# Load GROQ API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set up embeddings and LLM
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama3-70b-8192",
    max_tokens=5000
)

# Prompt
prompt_template = """You are an AI assistant. Use the following context to answer the user's question.
{context}
Question: {question}
Answer:"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

# UI Setup
st.set_page_config(page_title="AI PDF Q&A Bot 💬 - using LangChain", layout="centered")
st.title("📄 AI PDF Q&A Bot")
st.markdown("Upload a PDF and ask questions based on its content!")

uploaded_file = st.file_uploader("📤 Upload your PDF file", type=["pdf"])

if uploaded_file:
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Load and split PDF
    loader = PyPDFLoader(tmp_path)
    pages = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(pages)

    # Embed and create vector store
    with st.spinner("🔍 Creating vector store..."):
        db = FAISS.from_documents(docs, embedding_model)

    question = st.text_input("❓ Enter your question:")

    if question:
        with st.spinner("💬 Generating answer..."):
            docs = db.similarity_search(question)
            response = chain.run(input_documents=docs, question=question)
            st.markdown("### 💡 Answer:")
            st.write(response)
