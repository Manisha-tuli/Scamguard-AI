from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
def final_prompt(system_prompt):
    prompt=ChatPromptTemplate.from_messages([("system",system_prompt),
                                  ("user","{email_text}")
                                  ])
    return prompt