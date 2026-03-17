from fastapi import FastAPI
from pydantic import BaseModel
from model import predict, model_version
from logger import log_data

app = FastAPI()

class RequestData(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "ML API Running"}

@app.post("/predict")
def get_prediction(data: RequestData):
    result = predict(data.text)

    log = {
        "input": data.text,
        "output": result,
        "model_version": model_version
    }

    log_data(log)

    return log