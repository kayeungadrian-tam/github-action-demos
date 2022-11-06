from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

router = APIRouter()


notes = {
    "1": {
        "title": "My first note",
        "content": "This is the first note in my notes application",
    },
    "2": {
        "title": "Uniform circular motion.",
        "content": "Consider a body moving round a circle of radius r, wit uniform speed v as shown below. The speed everywhere is the same as v but direction changes as it moves round the circle.",
    },
}


@router.get("/")
def get_notes() -> dict:
    return {"data": notes}
