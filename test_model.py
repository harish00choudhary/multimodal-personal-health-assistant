import joblib

model = joblib.load("disease_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

text = "I feel dizzy, weak, sweating, and fainting"

vec = vectorizer.transform([text])
pred = model.predict(vec)

print("Prediction:", pred[0])
