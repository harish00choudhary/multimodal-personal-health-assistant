🧠 Multimodal Personal Health Assistant

An AI-powered personal health assistant that predicts possible diseases based on user-reported symptoms using Natural Language Processing (NLP) and Machine Learning. The application also provides a confidence score for each prediction and is deployed using Streamlit.



This project aims to assist users by:

* Accepting health symptoms in natural language
* Predicting the most likely disease
* Displaying a confidence score for transparency
* Providing a simple and interactive web interface


🧠 Model Training
- The dataset consists of diseases and associated symptoms.
- Symptoms are transformed into numerical vectors using NLP techniques.
- A supervised machine learning classifier is trained on the processed data.
- The trained model is serialized using joblib.

To retrain the model locally:
python train_model.py

🖥️ Running the Application

1. `pip install -r requirements.txt`
2. `streamlit run app.py`

## ⚠️ Download !! 
[Download disease_model.pkl](https://drive.google.com/file/d/1MJdVnUVv7f1Ur0joQHpgmWDC9Ctjjj5E/view)

## Output Explanation

- Predicted Disease: The most likely disease based on symptoms
- Confidence Score: Model certainty (probability) for the prediction Example: 0.88 → 88% confidence


## Author
- Harish Choudhary
- B.Tech CSE (AI)
- Aspiring Software & Machine Learning Engineer
