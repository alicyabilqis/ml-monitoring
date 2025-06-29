from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    example: str

@app.get("/")
def root():
    return {"status": "Model ready"}

@app.post("/infer")
def infer(input: Input):
    # dummy model response
    result = {"prediction": f"Processed: {input.example}"}
    return result
