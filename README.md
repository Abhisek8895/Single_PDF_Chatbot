# 📄 PDF Chatbot with Gemini Flash

A Streamlit-based chatbot that lets you upload a **single PDF** and interact with it using Google's **Gemini 1.5 Flash** model. The app extracts text from the PDF, splits it into chunks, builds embeddings, and answers your questions conversationally.

---

## 🚀 Features
- **Single PDF Upload** — Upload one PDF and start chatting immediately.
- **Chunking & Embeddings** — Splits documents into chunks and creates semantic embeddings for retrieval.
- **Gemini 1.5 Flash** — Uses Google Gemini Flash for fast, cost-effective responses.
- **Vector Search (FAISS)** — Efficient semantic retrieval of relevant chunks.
- **Streamlit UI** — Simple, scrollable chat interface with session-based chat history.

---
## 📂 Project Structure
```
├── app.py                 # Streamlit application (entrypoint)
├── utils.py               # Helper functions (PDF loading, splitting, embeddings, LLM init)
├── data/                  # Saved uploaded PDFs
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (GOOGLE_API_KEY) — NOT committed
└── README.md              # This file
```



---

## ⚙️ Installation

1. **Clone the repository**
```
git clone https://github.com/Abhisek8895/Single_PDF_Chatbot.git
cd Single_PDF_Chatbot
```

2. **Create and activate a virtual environment**
```
python -m venv venv

macOS / Linux
source venv/bin/activate

Windows
venv\Scripts\activate
```

3. **Install dependencies**
```
pip install -r requirements.txt
```
4. **Configure API key**  
Create a `.env` file in the project root and add:  

```
GOOGLE_API_KEY=your_google_api_key_here
```

You can get an API key from **Google AI Studio / Google Generative AI** (follow Google’s instructions for API access).

---

## ▶️ Usage
Start the Streamlit app:  

```
streamlit run app.py
```

Open the local URL shown in the terminal (usually `http://localhost:8501`), upload a PDF, then ask questions in the chat input.

---

## 🛠 How it works
1. The PDF is saved to `data/` and pages are loaded.
2. Pages are split into overlapping text chunks for context preservation.
3. Embeddings for chunks are created using Gemini embeddings.
4. Embeddings are stored in a FAISS vector store for fast similarity search.
5. On each user query, the most relevant chunks are retrieved and passed to Gemini (chat) to generate a contextual answer.
6. Chat history is kept in the session to supply conversational context.

---

## 📦 Dependencies
- streamlit
- langchain
- langchain-community
- langchain-google-genai
- google-generativeai
- faiss-cpu
- pypdf
- python-dotenv  

Install with:  

```
pip install -r requirements.txt
```

---

## 🔒 Notes
- **Do not commit** your `.env` or API keys to public repos.
- Pin package versions in `requirements.txt` for reproducible installs when deploying.
- For production, consider persistent vector storage (disk DB) rather than in-memory FAISS recreations on each run.

---

## ♻️ Future Improvements
- Support uploading and querying **multiple PDFs** in one session.
- Persist vectorstore and chat history across restarts.
- Add user authentication and per-user persistent sessions.
- Improve UI/UX: avatars, streaming token responses, better styling, mobile responsiveness.
- Add unit tests and CI checks.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 👋 Contribution
Contributions, issues and feature requests are welcome. Open a PR or issue on the repository.



