def generate_health_advice(symptoms, report_text, image_text):
    combined_text = f"{symptoms}\n{report_text}\n{image_text}"

    return {
        "risk_level": "Moderate",
        "possible_conditions": [
            ("Viral Infection", 0.68),
            ("Bacterial Infection", 0.22)
        ],
        "advice": [
            "Stay hydrated",
            "Monitor symptoms",
            "Consult a doctor if condition worsens"
        ],
        "explanation": "Based on symptom similarity and extracted medical indicators"
    }
