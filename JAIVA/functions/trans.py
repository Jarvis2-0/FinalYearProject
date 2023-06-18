from time import sleep
from googletrans import Translator
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition as sr
import os
import playsound
import time



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




def translategl(query):
    speak("sure sir")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("In which language you want to translate?")
    b = input("To_language: ")
    text_to_trans = translator.translate(query, src="auto",dest= b,)
    text = text_to_trans.text
    try:
        spk = gTTS(text=text, lang= b,slow= False)
        spk.save("voice.mp3")
        playsound("voice.mp3")
        time.sleep(5)
        os.remove("voice.mp3")
    except Exception as e:
        speak("sorry..Unable to translate..")

