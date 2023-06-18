import pyttsx3 as ttsx
import speech_recognition as sr
import requests



engine = ttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',240)


def speak(audio): 
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e: 
        speak("I could not understand, Please Say that again please...")
        return takecommand()  
    return query


def weather():
    speak("which citys weather you want to know sir?")
    city = takecommand().lower()

    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    speak(f"The Temperature of {city} is {format(temp2)} degree Celsius \nAnd the Weather is {format(temp1)}")