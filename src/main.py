from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
