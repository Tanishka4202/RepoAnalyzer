from fastapi import FastAPI
from scanner import scan_repository

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Backend Running"}


@app.get("/scan")
def scan():
    data = scan_repository(".")
    return data