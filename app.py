from fastapi import FastAPI
from data import CLASS

app = FastAPI()


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Server is up and running!"}


@app.get("/users")
def post_message(name: str):
    return {"message": f"Hello {name} from {CLASS}"}
