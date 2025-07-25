from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Load FAISS vector store
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

# Set up Groq LLM
llm = ChatGroq(temperature=0, model_name="llama3-8b-8192", api_key=groq_api_key)

# Set up RetrievalQA chain
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# User interaction loop
while True:
    query = input("🧠 Ask a question (or type 'exit' to quit): ")
    if query.lower() == "exit":
        break
    answer = qa.run(query)
    print("\n💡 Answer:\n", answer)
