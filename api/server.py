from fastapi import FastAPI
from pydantic import BaseModel
from app.model_loader import predict_anxiety
from app.preprocess import clean_text

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Exam Anxiety Detection API"}

@app.post("/predict")
def predict(data: InputText):

    cleaned = clean_text(data.text)

    label, confidence = predict_anxiety(cleaned)

    return {
        "prediction": label,
        "confidence": round(confidence * 100, 2)
    }