import pyttsx3
import speech_recognition as sr
import random

Greetings = ["hello", "hey", "get back to work", "are you there", "ok" "come online", "online"]
Greetings_res = ["always there for you sir", "i am ready sir", "always there for you", "how may i help you sir", "i am online and fully ready sir", "your wish my command"]




engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio): 
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#-------------------------------------#

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e: 
        speak("Say that again please...")
        return takecommand()
    
    return query


query = takecommand().lower()
def funtime():

    for word in Greetings:
        if word in query:
            speak(random.choice(Greetings_res))
