
# 🧠 AI PDF Q&A Bot using LangChain

A simple AI-powered application that allows users to ask questions based on the content of a PDF file. It leverages **LangChain**, **OpenAI's embeddings**, **FAISS vector store**, and **Streamlit** to provide context-aware answers from documents.

---

## 🚀 Features

- Upload any PDF and ask questions based on its content.
- Retrieves the most relevant sections of the PDF using vector similarity.
- Uses OpenAI's LLM to answer questions based on the document.
- Fast and responsive web interface built with Streamlit.

---

## 🛠️ Tech Stack

| Component        | Purpose                                                                 |
|------------------|-------------------------------------------------------------------------|
| **LangChain**    | Framework to handle document loading, splitting, and retrieval pipelines. |
| **OpenAI API**   | Used to generate answers using GPT models and create embeddings.        |
| **FAISS**        | Efficient similarity search in a vector database (used for document retrieval). |
| **Streamlit**    | Lightweight Python web framework to build the interactive UI.           |
| **PyMuPDF / fitz**| PDF reading and parsing.                                                |
| **dotenv**       | Loads environment variables (like API keys) from `.env` securely.       |

---

## 📁 Project Structure

```plaintext
AI-PDF-QnA-Bot-using-LangChain/
│
├── app.py                  # Main Streamlit app
├── qa_bot.py               # Core logic for processing PDF and answering queries
├── requirements.txt        # Python dependencies
├── .gitignore              # Files to exclude from version control
└── README.md               # You're reading this!
````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Nourin04/AI-PDF-QnA-Bot-using-LangChain.git
cd AI-PDF-QnA-Bot-using-LangChain
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a file named `.env` in the root folder:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ Make sure your `.env` file is **not pushed to GitHub**. It’s listed in `.gitignore` already.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the provided local URL in your browser (usually `http://localhost:8501`).

---

## 📌 How It Works

1. **Upload PDF** via Streamlit interface.
2. `qa_bot.py`:

   * Uses LangChain to load and split the PDF.
   * Converts chunks into vector embeddings using OpenAI.
   * Stores and searches using FAISS for context retrieval.
3. Uses OpenAI’s LLM to generate an answer based on top-matching PDF chunks.
4. Displays the final answer in the UI.

---




