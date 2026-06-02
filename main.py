

from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
import os
from utils.helper import pre_process,post_process,load_prompt_from_yaml
from schemas.spam_schema import SpamDetection
from prompts.prompt_template import final_prompt
import config.config
from config.config import get_llm 
from schemas.llm_schema import llm_with_schema



llm=get_llm()

llm= llm_with_schema(llm)


system_prompt= load_prompt_from_yaml(f"""prompts/{os.getenv("PROMPT_TYPE")}.yml""")
prompt_template= final_prompt(system_prompt)

email= """
Email:
Congratulations! You have won $5,000,000 in an international lottery.
Click this link immediately to claim your prize.
"""
chain= RunnableLambda(pre_process)|prompt_template|llm|RunnableLambda(post_process)
print(chain.invoke(email))         