from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2.5-72B-Instruct" ,
    task = "text-generation" 
)

model = ChatHuggingFace(llm = llm)


# first prompt -> detailed report
template1 = PromptTemplate(
    template = 'Write a detailed report on {topic} ' ,
    input_variables = ['topic']
)


#2nd prompt -> summary 
template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text. /n {text}' ,
    input_variables = ['text']

)


prompt1 = template1.invoke({'topic' :'black holes'})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'text' : result.content})

result1 = model.invoke(prompt2)

print("Detailed Report : " , result.content)
print("\n\nSummary : " , result1.content)