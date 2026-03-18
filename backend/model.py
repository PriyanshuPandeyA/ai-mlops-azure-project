model_version = "v1"

def predict(text):
    if "bad" in text.lower():
        return "negative"
    return "positive"