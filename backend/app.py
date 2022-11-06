from fastapi import FastAPI
from backend.data import CLASS

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}


@app.get("/users")
def post_message(name: str):
    return {"message": f"Hello {name} from {CLASS}"}
