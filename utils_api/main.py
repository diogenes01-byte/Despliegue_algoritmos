from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextRequest(BaseModel):
    texto: str

@app.post("/contar_palabras")
def contar_palabras(data: TextRequest):
    return {"palabras": len(data.texto.split())}

@app.post("/invertir_texto")
def invertir_texto(data: TextRequest):
    return {"invertido": data.texto[::-1]}

@app.post("/mayusculas")
def mayusculas(data: TextRequest):
    return {"mayusculas": data.texto.upper()}
