# main.py
from langchain.chains import ConversationalRetrievalChain
from utils import load_single_pdf, split_docs, create_vectorstore, get_llm

# Load and process PDF
pdf_path = "data/Sql With Python.pdf"
documents = load_single_pdf(pdf_path)
chunks = split_docs(documents)
vectorstore = create_vectorstore(chunks)

# Initialize LLM
llm = get_llm()

# Create conversation chain
retriever = vectorstore.as_retriever()
conversation = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever
)

# Chat loop
chat_history = []
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    result = conversation.invoke({"question": query, "chat_history": chat_history})
    print("Bot:", result["answer"])
    chat_history.append((query, result["answer"]))
