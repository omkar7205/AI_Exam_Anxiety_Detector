from transformers import BertTokenizer, BertForSequenceClassification
import torch

model = BertForSequenceClassification.from_pretrained("bert_anxiety_model")
tokenizer = BertTokenizer.from_pretrained("bert_anxiety_model")

def predict_anxiety(text):

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    outputs = model(**inputs)

    probs = torch.nn.functional.softmax(outputs.logits, dim=1)

    prediction = torch.argmax(probs).item()

    confidence = probs[0][prediction].item()

    if prediction == 1:
        result = "Anxiety Detected"
    else:
        result = "No Anxiety"

    return result, round(confidence * 100, 2)