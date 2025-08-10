# utils.py
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Please set GOOGLE_API_KEY in the .env file")


def load_single_pdf(uploaded_file):
    """Save uploaded PDF to 'data' folder and load it."""
    os.makedirs("data", exist_ok=True)  # Ensure 'data' folder exists
    file_path = os.path.join("data", uploaded_file.name)

    # Save the uploaded file to 'data'
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load the PDF
    loader = PyPDFLoader(file_path)
    return loader.load()


def split_docs(documents, chunk_size=1000, chunk_overlap=200):
    """Split documents into smaller chunks for embeddings."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)


def create_vectorstore(chunks):
    """Create a FAISS vector store from document chunks."""
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GOOGLE_API_KEY
    )
    return FAISS.from_documents(chunks, embeddings)


def get_llm(model_name="models/gemini-1.5-flash"):
    """Return a Google Generative AI chat model."""
    return ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=GOOGLE_API_KEY
    )
