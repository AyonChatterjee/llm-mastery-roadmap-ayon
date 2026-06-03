from langchain_huggingface  import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2.5-72B-Instruct" ,
    task = "text-generation" 
)

model = ChatHuggingFace(llm = llm)

# Create parser first
parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me 5 facts about {topic} \n {format_instructions}' ,
    input_variables = [],
    partial_variables = {'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser

result =chain.invoke({'topic' : 'black hole'})

print(result)