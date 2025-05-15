from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"],
        allow_headers=["*"],
    )