from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence , RunnableParallel

load_dotenv()


prompt1 = PromptTemplate(
    template = "Write a tweet on this {topic}" , 
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Write a LinkedIn post on this {topic}" ,
    input_variables = ['topic']
)

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.3-70B-Instruct" ,
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

parallel_chain = RunnableParallel( {
    'tweet' : RunnableSequence(prompt1 | model | parser),
    'linkedin_post' : RunnableSequence(prompt2 | model | parser)
})


result = parallel_chain.invoke({'topic': 'AI and the Future of Work'})

print(result['tweet'])
print(result['linkedin_post'])