from typing import Literal
from pydantic import BaseModel, Field

class SpamDetection(BaseModel):
    classification:Literal["SPAM","NOT SPAM"] = Field(description="Final classification of email.")
    reason:str=Field(description="Short reason for explaining why the email is spam or not spam")
    score: int = Field(description="confidence score -integer between 0 to 10")