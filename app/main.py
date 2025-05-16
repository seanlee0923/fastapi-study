from fastapi import FastAPI

from app.api import api_router
from app.core.cors import setup_cors
app = FastAPI()
setup_cors(app)
app.include_router(api_router)

@app.get("/")
async def index():
    return {"": "index page!"}
