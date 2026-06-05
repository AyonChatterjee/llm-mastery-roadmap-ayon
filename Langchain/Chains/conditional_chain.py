from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser 
from pydantic import BaseModel , Field
from typing import Literal

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task = "text-generation"
)

model1 = ChatHuggingFace(llm = llm1)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive' , 'negative'] = Field(description  = "Give me the sentiment of the feedback")


parser2 = PydanticOutputParser(pydantic_object = Feedback)    

prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following text into positive or negative \n{feedback} \n {format_instructions}', 
    input_variables = ['feedback'] , 
    partial_variables = {'format_instructions': parser2.get_format_instructions()}

)

classifier_chain = prompt1 | model1 | parser2

prompt2 = PromptTemplate(
    template = 'Write an appropriate response to the positive feedback: \n {feedback}',
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = 'Write an appropriate response to the negative feedback: \n {feedback}',
    input_variables = ['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment =='positive' , prompt2 | model1 | parser), 
    (lambda x:x.sentiment =='negative' , prompt3 | model1 | parser), 
    RunnableLambda(lambda x: "Invalid Sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback' : "I love 3 idiots"})

print(result)

chain.get_graph().print_ascii()