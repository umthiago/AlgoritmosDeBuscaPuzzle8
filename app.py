from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import time

from resultado import astar, greedy

app = FastAPI()

class RequestData(BaseModel):
    estado: list[int]
    algoritmo: str


@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/script.js")
def js():
    return FileResponse("script.js")


@app.get("/style.css")
def css():
    return FileResponse("style.css")


@app.post("/resolver")
def resolver(data: RequestData):

    start = time.time()

    if data.algoritmo == "astar":
        resultado = astar(data.estado)
    else:
        resultado = greedy(data.estado)

    end = time.time()

    resultado["tempo"] = round(end - start, 5)

    return resultado