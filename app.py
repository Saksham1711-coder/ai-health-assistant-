from flask import Flask, request, jsonify
import requests

# 🔑 PUT YOUR OPENROUTER KEY HERE
API_KEY = "PASTE_YOUR_NEW_KEY"

app = Flask(__name__)

def ask_ai(text):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": f"""
User symptoms: {text}

Give:
- possible issue
- what to eat
- what to avoid
- doctor
- emergency warning

Keep it short and clear.
"""
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    print("DEBUG:", result)

    if "choices" not in result:
        return "API error: " + str(result)

    return result["choices"][0]["message"]["content"]


@app.route("/predict", methods=["POST"])
def predict():
    text = request.json.get("text", "")
    output = ask_ai(text)
    return jsonify({"result": output})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)