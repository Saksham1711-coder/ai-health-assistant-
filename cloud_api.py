from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from feature_extractor import extract_features

app = Flask(__name__)
model = joblib.load("model.pkl")

def analyze(text):
    features = extract_features(text)
    arr = np.array([features])

    pred = model.predict(arr)[0]

    if pred == 1:
        return {"result": "High Risk", "advice": "Consult doctor"}
    else:
        return {"result": "Low Risk", "advice": "Stay healthy"}

@app.route("/predict", methods=["POST"])
def predict():
    text = request.json["text"]
    return jsonify(analyze(text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)