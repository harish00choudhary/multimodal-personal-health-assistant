import numpy as np

def analyze_text(text, model, vectorizer):
    text_vec = vectorizer.transform([text])
    probs = model.predict_proba(text_vec)[0]

    predicted_index = probs.argmax()
    confidence = probs[predicted_index] * 100
    prediction = model.classes_[predicted_index]

    return prediction, confidence

