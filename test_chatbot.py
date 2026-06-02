# Prompt
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv
import os

load_dotenv()

session_store = {}

def get_session_history(session_id:str):
  if(session_id not in session_store):
    session_store[session_id] = InMemoryChatMessageHistory()
  return session_store[session_id]

# 1. Define the chatprompt template
prompt_template = ChatPromptTemplate.from_messages([("system", "You're a helpful assistant, please answer in one line."),
                                  MessagesPlaceholder(variable_name = 'chat_history'),
                                 ("human", "{user_input}")])
# 2. Define your llm
llm = ChatOpenAI(model="gpt-4o-mini")

# 3.
parser = StrOutputParser()

# 4. Make the chain
chain = prompt_template|llm|parser

# Upgrade the chain
chat_chain = RunnableWithMessageHistory(chain, get_session_history,
                           input_messages_key = 'user_input', history_messages_key = 'chat_history')
#user_id = input("Enter the user_id")
def get_bot_response(user_text:str,session_id:str):
  config = {"configurable": {"session_id": session_id}}
  content = chat_chain.invoke({"user_input": user_text}, config = config)
  return content

# def get_bot_response(user_text:str, session_id:str):
#     config = {"configurable": {"session_id": session_id}}
#     content = chat_chain.invoke({"user_input": user_text}, config = config)
#     return content
print(get_bot_response("Hi How are You","123"))