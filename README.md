🧠 Multimodal Personal Health Assistant

An AI-powered personal health assistant that predicts possible diseases based on user-reported symptoms using Natural Language Processing (NLP) and Machine Learning. The application also provides a confidence score for each prediction and is deployed using Streamlit.

🚀 Project Overview

This project aims to assist users by:

- Accepting health symptoms in natural language

- Predicting the most likely disease

- Displaying a confidence score for transparency

- Providing a simple and interactive web interface

The system is designed as an end-to-end ML product, covering:

-> Data preprocessing

-> Model training

-> Model serialization

-> Web application deployment

🧩 Features

📝 Symptom-based disease prediction

📊 Confidence score for predictions

⚡ Fast inference using a lightweight ML model

🌐 Streamlit-based web interface

🧠 NLP-based text vectorization

🏗️ Tech Stack

- Programming Language: Python

- Machine Learning: Scikit-learn

- NLP: HashingVectorizer / TF-IDF

- Model Persistence: Joblib

- Web Framework: Streamlit

- Data Handling: Pandas, NumPy

📂 Project Structure
multimodal_health_assistant/
│
├── app.py                # Streamlit web application
├── train_model.py        # Model training script
├── test_model.py         # Model testing script
├── resume_parser.py      # Input processing utilities
├── matcher.py            # Prediction & confidence logic
├── requirements.txt      # Project dependencies
├── .gitignore            # Ignored files (models, venv, cache)
└── README.md             # Project documentation


⚠️ The trained model file (disease_model.pkl) is intentionally excluded from GitHub due to file size limits.

🧠 Model Training

- The dataset consists of diseases and associated symptoms.

- Symptoms are transformed into numerical vectors using NLP techniques.

- A supervised machine learning classifier is trained on the processed data.

- The trained model is serialized using joblib.

To retrain the model locally:

python train_model.py

🖥️ Running the Application
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit app
streamlit run app.py

📈 Output Explanation

- Predicted Disease: The most likely disease based on symptoms

- Confidence Score: Model certainty (probability) for the prediction
        Example: 0.88 → 88% confidence

⚠️ Disclaimer

This project is for educational and demonstration purposes only.
It is not a substitute for professional medical advice, diagnosis, or treatment.

👨‍💻 Author

Harish Choudhary
B.Tech CSE (AI)
Aspiring Software & Machine Learning Engineer

🌟 Future Enhancements

Top-3 disease predictions

1. Risk level classification

2. Doctor/specialist recommendation

3. Multimodal input (text + reports/images)
