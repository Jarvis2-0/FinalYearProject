import pyttsx3
import speech_recognition as sr
import requests


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



def MY_loc():
            speak("let me check..It may take a while..please Wait sir! ")
            try:
                locate = requests.get('https://api.ipify.org').text
                url_loc = 'https://get.geojs.io/v1/ip/geo/'+locate+'.json'
                geo_requests = requests.get(url_loc)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir i am not sure but i think we are in {city} city of {country} country.")
            except Exception as e: 
                speak("Sorry sir due to poor network connectivity i am not able to locate us..")
                pass
