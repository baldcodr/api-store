from fastapi import FastAPI
from api.store.firestore import get_document_by_id, add_person,read_all_docs
from api.store.schema import Person
from typing import Dict

app = FastAPI()

@app.get("/")
def healthcheck():
    return 'Health - OK'

@app.get("/data/{id}")
async def read_person(id: str):
    try:
        data = get_document_by_id("persons",id)
    except Exception as e:
        return (f"ERROR: {e}")
    
    return f"Data retrieved successfully - {data}"

@app.post("/new")
async def post_person(person: Person):
    try:
        result = person.to_dict()
        add_person(result)
    except Exception as e:
        return (f"ERROR: {e}")
    return f"Data stored successfully - {result['id']}"

