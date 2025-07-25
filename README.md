
# AI PDF Q&A Bot using LangChain & Groq API

This is a lightweight PDF Question-Answering Bot that lets you upload any academic or general-purpose PDF and ask questions based on its content. It uses **Groq's blazing-fast API with LLaMA 3** for answering, and **LangChain** for document processing and retrieval.

---

## ✅ Features

- Upload and analyze **PDF** documents.
- Ask **natural language questions** based on document content.
- Uses **Groq API with Meta’s LLaMA 3** — much faster than OpenAI.
- Extracts, chunks, embeds, and searches document content using **FAISS**.
- Clean and interactive UI with **Streamlit**.

---

## 🛠️ Tech Stack

| Tool/Library     | Purpose |
|------------------|---------|
| **LangChain**    | Framework for chaining LLM + document processing. |
| **Groq API**     | LLM backend using `llama3-8b-8192`. |
| **FAISS**        | Local vector database for semantic search. |
| **PyMuPDF** (`fitz`) | Extract text from PDFs. |
| **Streamlit**    | Frontend web app UI. |
| **dotenv**       | Manage secrets like Groq API keys. |

---

## 📂 Project Structure

```bash
AI-PDF-QnA-Bot-using-LangChain/
│
├── app.py                    # Main Streamlit app
├── qa_bot.py                 # Handles loading, chunking, embedding, querying PDFs
├── generate_vector_store.py  # Script to precompute vector store (optional)
├── faiss_index/              # FAISS vector DB (auto-created)
├── requirements.txt          # Required dependencies
├── .env                      # Your Groq API key (not to be pushed to GitHub)
└── README.md                 # Project documentation
````

---

## 🔐 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Nourin04/AI-PDF-QnA-Bot-using-LangChain.git
cd AI-PDF-QnA-Bot-using-LangChain
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # For Windows
# or
source venv/bin/activate  # For macOS/Linux
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Add Your Groq API Key

Create a `.env` file in the root folder with the following:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can get your API key from [https://console.groq.com/keys](https://console.groq.com/keys)

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

This will open the bot in your browser at `http://localhost:8501`.

---

## ⚙️ How It Works

1. **PDF Upload** – Users upload a PDF via the UI.
2. **Text Extraction** – The app extracts and splits the text into manageable chunks.
3. **Vectorization** – FAISS creates embeddings and stores them locally.
4. **Q\&A** – When a question is asked, relevant chunks are retrieved using vector similarity and passed to the Groq-powered LLM for answering.

---

## ❌ .gitignore Tips

Ensure the following files are ignored in Git:

```gitignore
venv/
.env
__pycache__/
*.pyc
faiss_index/
```

---


## 📌 Future Ideas

* Multi-file PDF support
* Highlighting answer context inside the document
* Caching API responses
* Add chat memory using LangChain

