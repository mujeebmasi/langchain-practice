from langchain_huggingface import HuggingFaceEmbeddings


embedings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

texts = ["Hello world", "Hi there"]
vectors = embedings.embed_documents(texts)
print(vectors)
