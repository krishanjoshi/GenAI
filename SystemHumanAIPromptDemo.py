from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

#create the object of llm
llm = ChatOllama(
    model="llama3")

#create the touple for message
# messages = [
#     (
#         "system",
#         "You are a very famous hindi song writter, with bollywood song writer experience of 20 years",
#     ),
#     ("human", "Write a 4 lines bhajan on Radha Krishna that will become a viral hit in india. it should be a new song."),
# ]

messages = [
    SystemMessage("You are a very famous hindi song writter, with bollywood song writer experience of 20 years"),
    HumanMessage ( "Write a 4 lines bhajan on Radha Krishna that will become a viral hit in india. it should be a new song.")
]

#invoke the message and get response.
while True:
    prompt = input(">>> Enter your prompt: ")

    if prompt.lower() == 'bye':
        break

    messages = [
    SystemMessage("You are a very famous hindi song writter, with bollywood song writer experience of 20 years"),
    HumanMessage ( prompt)
]
    response = llm.invoke(messages)
    #Print the response.content.
    print(response.content)

print("Thanks for using the service.")
