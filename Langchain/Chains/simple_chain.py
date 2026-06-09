from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser , ResponseSchema


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2.5-72B-Instruct" ,
    task = "text-generation" 
)

model = ChatHuggingFace(llm = llm)

schemas = [
    ResponseSchema(name = "facts" , description = "List of 5 interesting facts about the topic")
]
parser = StructuredOutputParser.from_response_schemas(schemas)

prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}.\n{format_instructions}' , 
    input_variables = ['topic'] , 
    partial_variables = {
        'format_instructions': parser.get_format_instructions()
    }
)

chain = prompt | model | parser

result = chain.invoke({'topic':'space exploration'})

print(result)

chain.get_graph().print_ascii()