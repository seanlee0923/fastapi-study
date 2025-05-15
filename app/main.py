from fastapi import FastAPI
from app.core.cors import setup_cors
app = FastAPI()
setup_cors(app)

@app.get("/")
async def index():
    return {"": "index page!"}
