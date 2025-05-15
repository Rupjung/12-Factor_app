from fastapi import FastAPI

from app.model import load_model, predict_quality
from app.schemas import WineInput

app = FastAPI()
model = load_model()


@app.post("/predict")
def predict(data: WineInput):
    result = predict_quality(model, data)
    return {"prediction": result}
