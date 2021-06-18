from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app.dbconfig import engine
from app.router import init_routes

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_routes(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}

