from fastapi import FastAPI
from pydantic import BaseModel
from backend.model import predict, model_version
from backend.logger import log_data
import time

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Customer Feedback API Running"}

@app.post("/predict")
def predict_api(data: InputData):
    start = time.time()

    result = predict(data.text)

    end = time.time()

    log = {
        "input": data.text,
        "output": result,
        "model_version": model_version,
        "response_time": end - start
    }

    log_data(log)

    return log