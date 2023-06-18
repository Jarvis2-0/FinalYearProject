import pyttsx3
import speech_recognition as sr
import requests
from requests import get

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


#-----------News_function_-----------------------#

def news():
    try:
        speak("What topic you need the news about? choose from below list:\n 1:Sport\n 2:Business\n 3:Entertainment\n 4:Health\n 5:Science\n 6:Technology")
        topic = takecommand().lower()
        url = ("https://newsapi.org/v2/top-headlines?country=in&category="+topic+"&apiKey=83c3f656a09a4e81ae875c67015419e6")
       
        main_page = requests.get(url).json()
        articles = main_page["articles"]
        topic = []
        day=["first", "second", "Third", "Fourth", "Fifth"]
        for ar in articles:
            topic.append(ar["title"])
        for i in range (len(day)):
            speak(f"The {day[i]} news is : {topic[i]}")
    
    except Exception as e: 
        speak("Sorry Sir! i cant find the news for today..")
       
#---------------------------------------------------------------------#

#-------------------News----------------------------------------------#


    # newsapi = NewsApiClient(api_key='5840b303fbf949c9985f0e1016fc1155')
    # 
    # topic = takecommand()
    # data = newsapi.get_top_headlines(q=topic, language="en", page_size=5)
    # newsData = data["articles"]
    # for y in newsData:
    #     speak(y["description"])