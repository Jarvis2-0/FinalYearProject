import pyttsx3
import speech_recognition as sr
import PyPDF2
from gtts import gTTS
from googletrans import Translator
import playsound



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 150)
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

#--------------------------------------------#

def pdfread():
    try:
        book = open("pdfs/book.pdf","rb")
        pdfReader = PyPDF2.PdfReader(book)
        pages =len(pdfReader.pages)
        speak(f"Total number of pages in this book are: {pages}")
        speak("Tell the page number i have to read from?")
        pg = int(input("Enter the page number: "))
        page = pdfReader.pages[pg] 
        text = page.extract_text()
        speak(text)
    except Exception as e:
        print(e)
        speak("I could not find any pdf sir..")






