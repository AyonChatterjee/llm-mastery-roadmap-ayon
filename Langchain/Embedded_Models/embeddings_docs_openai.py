from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model = "text-embedding-3-large" , dimensions = 32)

documents = [
    "Delhi is the capital of India.",
    "Paris is the capital of France.",
    "Tokyo is the capital of Japan."
]

results = embeddings.embed_documents(documents)

print(str(results))