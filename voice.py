import speech_recognition as sr
import pyttsx3
import requests

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except:
        return ""

def get_response(text):
    try:
        res = requests.post("http://127.0.0.1:5000/predict", json={"text": text})
        return res.json()["result"]
    except:
        return "Server error"

# 🚀 MAIN LOOP
speak("Hello, tell me your symptoms")

while True:
    text = listen()

    if text == "":
        continue

    if "stop" in text.lower():
        speak("Goodbye")
        break

    response = get_response(text)
    speak(response)