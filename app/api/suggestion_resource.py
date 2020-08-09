from fastapi import Header, APIRouter

from app.models.suggestions import Suggestions

suggestions_resource = APIRouter()

fake_suggestion_db = []

@suggestions_resource.post('/', status_code=201)
async def add_suggestion(payload: Suggestions):
    suggestion = payload.dict()
    fake_suggestion_db.append(suggestion)
    return {'id': len(fake_suggestion_db) - 1}
