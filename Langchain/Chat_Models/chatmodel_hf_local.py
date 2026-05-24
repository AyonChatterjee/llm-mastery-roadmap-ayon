from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(model_id="Qwen/Qwen2.5-72B-Instruct" , task = "text-generation" , pipeline_kwargs =dict(temperature = 0.8 , max_new_tokens = 10))

model = ChatHuggingFace(llm = llm)

result = model.invoke("What is the capital of France?")

print(result.content)