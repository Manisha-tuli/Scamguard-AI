from dotenv import load_dotenv
load_dotenv()
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

load_dotenv()

LLM_PROVIDER="OPENAI"
def get_llm():
    if(os.getenv("LLM_PROVIDER")=="OPENAI"):
        llm= ChatOpenAI(model="gpt-4o-mini")
        return llm
    elif(os.getenv("LLM_PROVIDER"=="GOOGLE")):
        llm= ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)
        return llm