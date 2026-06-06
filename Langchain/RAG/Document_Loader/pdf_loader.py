from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("/Users/ayonchatterjee/Desktop/LLMs-and-RAG-Tutorial/Langchain/RAG/Document_Loader/dl-curriculum.pdf")

docs = loader.load()

print(docs[0].page_content)
print(docs[1].metadata)