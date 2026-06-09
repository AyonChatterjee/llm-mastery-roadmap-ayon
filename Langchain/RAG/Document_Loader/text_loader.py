from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.3-70B-Instruct" ,
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

prompt = PromptTemplate(
    template = "Write a summary of the poem -\n {poem}",
    input_variables = ['poem']
)

parser = StrOutputParser()

loader = TextLoader('/Users/ayonchatterjee/Desktop/LLMs-and-RAG-Tutorial/Langchain/RAG/Document_Loader/cricket.txt' , encoding = 'utf-8')

docs = loader.load()

print(docs)

print(docs[0].page_content)
print(docs[0].metadata)


chain = prompt | model | parser

result = chain.invoke({'poem' : docs[0].page_content})

print(result)