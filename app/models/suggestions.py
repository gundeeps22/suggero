from datetime import datetime
from pydantic import BaseModel


from app.models.enums import Grade

class Suggestions(BaseModel):
    id: int
    suggestion: str
    author: str
    answered_question: int
    scope: Grade
    date_submitted: datetime
