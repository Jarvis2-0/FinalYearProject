import pyttsx3 as ttsx
import datetime
import time
import playsound



engine = ttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',240)


def speak(audio): 
    engine.say(audio)
    print(audio)
    engine.runAndWait()
        

def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
         speak('Good Morning sir!')
        elif hour>=12 and hour<18:
         speak('Good Afternoon sir!')
        else:
         speak('Good Evening sir!')
        c_time = time.strftime("%I:%M %p")
        speak(f"currently it is {c_time},lets do some work!!! How may i assist you?" )