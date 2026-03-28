from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3",
    top_p=0.1
    # other params...
)

prompt= "write a viral linkdin tweet on AI. "

response  =llm.invoke(prompt)

print(response.content)
