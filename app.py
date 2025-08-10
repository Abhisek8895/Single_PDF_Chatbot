import asyncio

# Fix for "no current event loop" in Streamlit
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


import streamlit as st
from utils import load_single_pdf, split_docs, create_vectorstore, get_llm
from langchain.chains import ConversationalRetrievalChain

# --- Streamlit App ---
st.set_page_config(page_title="📄 PDF Chatbot", page_icon="🤖")
st.title("📄 Single PDF Chatbot")

# File upload
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")


if uploaded_file:
    with st.spinner("Processing PDF..."):
        # Load and split PDF
        documents = load_single_pdf(uploaded_file)
        chunks = split_docs(documents)

        # Create vector store
        vectorstore = create_vectorstore(chunks)

        # Get retriever
        retriever = vectorstore.as_retriever()

        # Initialize LLM
        llm = get_llm()

        # Create conversation chain
        conversation = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever
        )

        # Session state for chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Chat interface
        query = st.text_input("Ask a question about your PDF:")
        if query:
            result = conversation.invoke({"question": query, "chat_history": st.session_state.chat_history})
            st.session_state.chat_history.append((query, result["answer"]))

        # Display chat history
        for i, (q, a) in enumerate(st.session_state.chat_history):
            st.markdown(f"**🧑:** {q}")
            st.markdown(f"**🤖:** {a}")