from fastapi import FastAPI
from datetime import datetime
from typing import List

from app.models.suggestions import Suggestions
from app.models.enums import Grade
from app.api.suggestion_resource import suggestions_resource

app = FastAPI()

app.include_router(suggestions_resource, prefix="/v1/suggestions")
