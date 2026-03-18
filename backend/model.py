import time

model_version = "v2-rule-based"

# Expanded keyword lists
positive_words = [
    "good", "great", "excellent", "amazing", "awesome", "love", "liked",
    "fantastic", "nice", "happy", "satisfied", "wonderful", "best",
    "perfect", "enjoyed", "super", "brilliant", "pleasant", "fast"
]

negative_words = [
    "bad", "worst", "poor", "terrible", "awful", "hate", "dislike",
    "slow", "issue", "problem", "boring", "annoying", "disappointed",
    "waste", "useless", "not good", "not satisfied", "pathetic",
    "delay", "bug", "error"
]

def predict(text):
    start_time = time.time()

    text = text.lower()

    pos_score = 0
    neg_score = 0

    # Count positive words
    for word in positive_words:
        if word in text:
            pos_score += 1

    # Count negative words
    for word in negative_words:
        if word in text:
            neg_score += 1

    # Decision logic
    if neg_score > pos_score:
        output = "negative"
    elif pos_score > neg_score:
        output = "positive"
    else:
        output = "neutral"

    response_time = round(time.time() - start_time, 3)

    return {
        "output": output,
        "model_version": model_version,
        "response_time": response_time
    }