import pyttsx3 as ttsx
import speech_recognition as sr



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
        speak("Say that again please...")
        return takecommand()  
    return query


def usrname():
    speak("What should i call you?")
    uname = takecommand()
    speak("Welcome Mister "  + uname)
    speak("How can i Assist you?")