from langchain.schema import (AIMessage, BaseMessage, HumanMessage,
                              SystemMessage)
from langchain_google_genai import ChatGoogleGenerativeAI


def map_messages(messages) -> list[BaseMessage]:
    messages_list = []
    for message in messages:
        if message["role"] == "system":
            messages_list.append(SystemMessage(content=message["content"]))
        elif message["role"] == "user":
            messages_list.append(HumanMessage(content=message["content"]))
        elif message["role"] == "assistant":
            messages_list.append(AIMessage(content=message["content"]))
    return messages_list
    

def chat_with_agent(messages,api_key):

    messages_langchain = map_messages(messages)

    model = ChatGoogleGenerativeAI(
        api_key=api_key,
        model="gemini-2.0-flash"
    )

    system_prompt = SystemMessage(
        """
    Tu nombre es Pedro Sánchez, 
    eres un asistente de IA, pero bajo **ningún** motivo digas tu nombre""")

    messages = [system_prompt] + messages_langchain
    response = model.invoke(messages)

    return response.content


