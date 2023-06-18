import pyttsx3 as ttsx
import speech_recognition as sr
from PyDictionary import PyDictionary as dicti





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

def dict():
    speak("Tell me the problem!")
    prob1 =takecommand().lower()

    if 'meaning' in prob1:
        prob1 = prob1.replace('what is the', "")
        prob1 = prob1.replace('Jessi', "")
        prob1 = prob1.replace("meaning of","")
        result1 = dicti.meaning(prob1)
        speak(f'The Meaning of {prob1} is {result1}')

    speak('Exited Dictonary!!!')