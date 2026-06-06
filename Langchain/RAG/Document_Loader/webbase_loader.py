from langchain_community.document_loaders import  WebBaseLoader
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
    template = 'Answer the following question \n {question} from the following text - \n {text}' , 
    input_variables = ['question' , 'text']
)

parser = StrOutputParser()


url = 'https://www.amazon.in/Google-Pixel-10a-Obsidian-Storage/dp/B0GP88QJL8/ref=sr_1_1?crid=85Q0OHTU4OF4&dib=eyJ2IjoiMSJ9.8Rnw77npyoiJoFrWqZrPuFET2GVja8EyDZ646oeLqyb5q42YSPGXAlp51VVo0Bf_-nQQJNKbgogSRqzNuQ8CGwUMtfuNtd8jtQplF0Oh1SU4Ygs02-h0sw2KtM-z28iP4FL9-ZmtN8Qqghrc7e569CJck7vNmxJTjExNaFLKp2tvvkpOmlZx4qEV6NDarVYO2J5xmjDrGWz1fetdmVT46rAllvn4vtU1VZbFxp7IRbQ.3FfJAtGtOjx55lXMs5sKHkRH_Zzbm3j0CXyoF00gce8&dib_tag=se&keywords=google+pixel&qid=1780771214&sprefix=gg%2Caps%2C271&sr=8-1'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question' : 'Price of the Phone' , 'text' : docs[0].page_content}))