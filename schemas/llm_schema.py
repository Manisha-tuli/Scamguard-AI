from schemas.spam_schema import SpamDetection
def llm_with_schema(llm):
 llm_with_schema = llm.with_structured_output(SpamDetection)
 return llm_with_schema