model_version = "v1"

def predict(text: str):
    if "good" in text:
        return "positive"
    return "negative"