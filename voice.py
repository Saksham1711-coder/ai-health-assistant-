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
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
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

speak("Tell me your symptoms")

while True:
    text = listen()

    if text == "":
        continue

    if "stop" in text.lower():
        speak("Goodbye")
        break

    if "chest pain" in text.lower():
        speak("Warning: This could be serious. Please seek medical help.")

    response = get_response(text)
    speak(response)