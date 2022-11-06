from fastapi import FastAPI


from .routes import router
from backend.data import CLASS

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome!"}


@app.get("/users")
def post_message(name: str):
    return {"message": f"Hello {name} from {CLASS}"}


app.include_router(router, prefix="/note")
