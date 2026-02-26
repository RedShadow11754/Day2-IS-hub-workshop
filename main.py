from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
import os

documents = [
    "I'm Abel Alemu (aka Junior) I'm learning IS at Addis Ababa University",
    "I've done a lot of fun projects, especially using Python.",
    "I'm enjoying learning RAG in this workshop, I'm learning a lot of things and it's truly an amazing experience.",
    "I've had a few achievements in this not-so-short life of mine, and hopefully, many more are yet to come.",
    "I have a dream to be a successful AI-focused developer and have a calm life. yup that's my goal",
]

doc = [Document(page_content=document) for document in documents]

model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

persist_dir = "./chroma_db"
if os.path.exists(persist_dir):
    vector_store = Chroma(
        persist_directory=persist_dir,
        embedding_function=model
    )
else:
    vector_store = Chroma.from_documents(
        documents=doc,
        embedding=model,
        persist_directory=persist_dir
    )
    vector_store.persist()

def search(query,top_k=1):
    print(f"\n🔎 Query: {query}")
    print(f"Top-K: {top_k}")

    results = vector_store.similarity_search(query, k=top_k)
    for i,result in enumerate(results):
        print(f"Result{i+1}. {result.page_content}")

search(query="Where and what does Abel learn",top_k=2)
search(query="What's Abel's dream",top_k=2)
search(query="How is Abel doing with the RAG workshop?")