def extract_features(text):
    text = text.lower()

    features = {
        "age": 50,
        "sex": 1,
        "cp": 0,
        "trestbps": 120,
        "chol": 200,
        "fbs": 0,
        "restecg": 0,
        "thalach": 150,
        "exang": 0,
        "oldpeak": 0.0,
        "slope": 1,
        "ca": 0,
        "thal": 2
    }

    if "chest pain" in text:
        features["cp"] = 2
    if "high bp" in text:
        features["trestbps"] = 150
    if "cholesterol" in text:
        features["chol"] = 250

    return list(features.values())