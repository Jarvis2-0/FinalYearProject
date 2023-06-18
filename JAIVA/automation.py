# import pyttsx3
# import speech_recognition as sr
# import requests
# import geopy
# from geopy.distance import great_circle
# from geopy.geocoders import Nominatim
# import geocoder
# import webbrowser



# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[0].id)

# def speak(audio): 
#     engine.say(audio)
#     print(audio)
#     engine.runAndWait()
# #-------------------------------------#

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 2
#         r.energy_threshold = 300
#         audio = r.listen(source,0,4)

#     try:
#         print('Recognizing...')
#         query = r.recognize_google(audio, language='en-in')
#         print(f"user said: {query}\n")

#     except Exception as e: 
#         speak("Say that again please...")
#         return takecommand()
    
#     return query



# def Gm(place):
#     url_place = 'https://www.google.com/maps/place/'+str(place)
#     geolocator = Nominatim(user_agent="myGeocoder")


#     location = geolocator.geocode(place, addressdetails = True)

#     target_loc = location.latitude, location.longitude
#     webbrowser.open(url=url_place)
#     location = location.raw['address']

#     target = {'city': location.get('city',''),
#               'state': location.get('state',''), 
#               'country' : location.get('country',"")}

#     current_loc = geocoder.ip('me')

#     current_location = current_loc.latlng

#     distance = str(great_circle(current_location,target_loc))
#     distance = str(distance.split(' ',1)[0])
#     distance = round(float(distance),2)

#     speak(target)
#     speak(f"sir, {place} is {distance}")

# Gm('mumbai')