import pyttsx3   #For installing all these mentioned modules use pip command in shell E.g:-pip isntall pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
from pywikihow import search_wikihow
import numpy as np
from PIL import Image, ImageGrab
import requests
from requests import get
import pywhatkit as kit
import psutil
import pyautogui
import time
import playsound
from PIL import Image
import pyjokes
import subprocess, sys
#-----------------Memory-----------#
user = "Akshay"
timetable = ["schedule", "do i have plans", "tell me todays plans", "report my schedule", "am i busy" ]
Greetings = ["hello", "hey", "get back to work", "are you there", "ok" "come online", "online"]
#-------------------------------------#


#---------------Text to speech run engine---------#
engine = pyttsx3.init()         #call pyttsx3 function (python text to speech version 3)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)   #To set voices system default For male =0 and for female = 1

#------------Speak function---------#

def speak(audio): 
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#-------------------------------------#

#-------------Take command function-------#

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2     #for pause in listening
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

#----------------------------------------------#

#-----------Startup-----------------------------#
# from intro import play_gif
# play_gif
# playsound.playsound("plug_in.mp3")
#-----------------------------------------------#

#----------Main Function-------------------#

def taskexecution():  
    pyautogui.press('Esc')
    playsound.playsound('songs/accessgranted.mp3')
    from functions.intro import play_gif
    play_gif
    playsound.playsound("songs/plug_in.mp3")
    from functions.wakeup import wishme
    wishme()
    while True:
    # if 1 : ----> to get query execute only once<----
        query = takecommand().lower()

        if 'wake up' in query:
            from functions.wakeup import wishme
            wishme()
        if 'my name' in query:
            from functions.changename import usrname
            usrname()
#-------------------------------------------------#

#---------Commands for assistant-------#

#---> To search on wikipidea<---
        elif 'wikipedia' in query:
            try:
                speak('Searching on wikipidea....')
                query = query.replace('wikipidea', '')
                results = wikipedia.summary(query, sentences=2)
                speak(f"according to wikipidea:- {results}")
            except Exception as e: 
             speak("Say that again please...")

#---> to get current date & time<---
        elif 'time'   in query:
            try:
                from datetime import datetime
                now = datetime.now()
                current_time = now.strftime("%I:%M:%S %p")
                speak("Sir Current Time is: " + current_time)
            except Exception as e: 
             speak("I cant get you!")

        elif 'date' in query:
            try:
                from datetime import datetime
                speak("Todays date is " + str(datetime.now().day)
                    + " " + str(datetime.now().month)
                    + " " + str(datetime.now().year))
            except Exception as e: 
             speak("I cant get you!")
            
#---> to get the weather Report<---
        elif 'weather' in query:
            try:
                from functions.weather import weather
                weather()
            except Exception as e: 
             speak("Say that again please...")

#---> to get the latest news on any topic<---
        elif "news" in query or "headlines" in query:
            try:
                from functions.news import news
                news()
            except Exception as e:
                speak("Try after some time..!")
            
#---> to listen some jokes by pyhton<---   
#      
        elif "joke" in query:
            speak(pyjokes.get_joke())

#--------Location------------#

        elif "location" in query or 'where we are' in query:
            try:
                from functions.loc import MY_loc
                MY_loc()
            except Exception as e: 
             speak("Say that again please...")

#For finding the place on google maps----#

        elif "where is" in query:
            try:    
                query = query.replace("where is", "")
                location = query
                speak(f"Locating {location}, Please wait sir")
                webbrowser.open("https://www.google.com/maps/place/" + location + "")
            except Exception as e: 
             speak("sorry sir. I could not locate where it is please say it again...")

#-------Random words-------------#
        elif f'{random.choice(Greetings)}' in query:
            try:
                from functions.fun import funtime
                funtime() 
            except Exception as e: 
             speak("Say that again please...")   

#-----to change the password----------#
        elif "change password" in query:
            try:
                speak("Whats the new password?")
                newPass= input("Enter the new password:")
                newPassword = open("text_files/pass.txt","w")
                newPassword.write(newPass)
                newPassword.close()
                speak("Done Sir! Your password has been changed successfully!")
            except Exception as e: 
             speak("Password not changeable please try again")
            
#---> to Schedule your day<---       
        elif "schedule my day"in query or "make my" in query:
            try:   

                tasks =[]
                speak("Do you want to clear all old schedules? Say Yes / No")
                query = takecommand().lower()
                if "yes" in query:
                    file = open("text_files/schedules.txt", "w")
                    file.write(f"")
                    file.close()
                    no_tasks = int(input("Enter the Number of tasks: "))
                    i = 1
                    for i in range(no_tasks):
                        tasks.append(input("Enter the task: "))
                        file = open("text_files/schedules.txt","a")
                        file.write(f"{i}. {tasks[i]}\n")
                        file.close()
                        
                elif "no" in query:
                    i = 1
                    no_tasks = int(input("Enter the Number of tasks: "))
                    for i in range(no_tasks):
                        tasks.append(input("Enter the task: "))
                        file = open("text_files/schedules.txt","a")
                        file.write(f"{i}. {tasks[i]}\n")
                        file.close()
                speak("Your task has been saved successfully!")
            except Exception as e: 
             speak("please say it again...")

        elif f'{random.choice(timetable)}' in query:
                file = open("text_files/schedules.txt")
                content =file.read()
                file.close()

                title = "Schedules"  
                command = f'''
                osascript -e 'display notification "{content}" with title "{title}"'
                '''
                os.system(command)
                playsound.playsound("songs/noti.mp3")

#-----for opening and closing apps Easy method-----#
        elif 'open' in query:
            try:
                query = query.replace("open","")
                pyautogui.hotkey("command","space")
                pyautogui.typewrite(query)
                pyautogui.sleep(2)
                pyautogui.press("enter")
                speak(f"{query} opened!")
            except Exception as e: 
             speak("Say it again please...")

        elif 'close' in query:
            try:
                query = query.replace("close","")
                speak(f"Ok sir! Closing {query}...")
                pyautogui.hotkey("Option","command","w")
                pyautogui.sleep(2)
            except Exception as e: 
             speak("Say that again please...")

#-----------For switching window----------------------#

        elif "switch" in query:
            try:
                speak("Switching window")
                pyautogui.keyDown("command")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("command")
            except Exception as e: 
             speak("try again...")
              
#--------For play/stop music--------#
        elif 'play music' in  query:
            try:
                speak("Enjoy the music..") 
                subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Resso.app"])  
                
        
            except Exception as e:
               #print(e)
               speak('Sorry sir, I am not able to play music')
        elif 'stop music' in  query:  
            os.system("pkill Resso")

#---------to search anything on google----#       
        elif 'google' in  query or "Google"in query:
            try:
                speak("sir, what should i search on google") 
                webbrowser.open("https://www.google.com/search?q=" +takecommand())
                speak("Here is your search")
            except Exception as e: 
             speak("Say that again please...")


        elif 'close google' in  query:  
            os.system("pkill Chrome")

        elif 'youtube' in query:
            try:
                speak("What you want to search on youtube, sir!")
                kit.playonyt(takecommand())
                speak("Enjoy Your Time, sir!")
            except Exception as e: 
             speak("Say that again please...")

        elif 'facebook' in query:
            try:
                controller = webbrowser.get()
                controller.open("https://www.facebook.com/")
            except Exception as e: 
             speak("Say that again please...")

        elif 'instagram' in query:
            try:
                controller = webbrowser.get()
                controller.open("https://www.instagram.com/")
            except Exception as e: 
             speak("Say that again please...")
    
        elif 'gmail' in query:
            try:
                controller = webbrowser.get()
                controller.open("https://accounts.google.com/AccountChooser/identifier?flowName=GlifWebSignIn&flowEntry=AccountChooser")
            except Exception as e: 
             speak("Say that again please...")

#-------------to capture the photo------#

        elif 'click' in query or "picture" in query or  "capture" in query:
            try:
                pyautogui.hotkey("command","space")
                pyautogui.typewrite("photo Booth")
                pyautogui.sleep(2)
                pyautogui.press("enter")
                pyautogui.sleep(2)
                speak("Smile please!")
                pyautogui.hotkey("command","shift","t")
                speak("Looking nice!!")
                pyautogui.sleep(8)
                os.system("pkill Photo Booth")
            except Exception as e: 
             speak("Try it  again please...")

#---------------for translating anything from one lang to another lang-------------------------#

        elif "translate" in query:
            try:
                from functions.trans import translategl
                query = query.replace("translate","")
                translategl(query)  
            except Exception as e: 
             speak("Say it again please!...")  

#-------------Battery Percentage----------#
        elif "battery" in query or "percentage" in query:
            try:
                battery_per = psutil.sensors_battery().percent
                speak(f"Power is {battery_per}% remaining..")
                if int(battery_per)==30 :
                    speak('Your system is low of power.. please charge')
                elif int(battery_per)<10 :
                    speak('Your system is very low of power.. please charge otherwise system willl shutdown very soon..')
                else:
                    speak('your System has enough Power!')
            except Exception as e:
                speak("Sorry.. say it again.")

#--- to know the cpu statistics----#
        elif "cpu" in query:
            try:
                speak(f"Cpu is running at  {str(psutil.cpu_percent())} %")
            except Exception as e: 
             speak("try again...")

#------------Internet Speed--------------#
        elif 'internet speed' in query:
            try:
                i_s = ((psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent )/psutil.net_io_counters().bytes_sent)
                st_up = (psutil.net_io_counters().bytes_recv/psutil.net_io_counters().bytes_sent)
                st_dw = (psutil.net_io_counters().bytes_sent/psutil.net_io_counters().bytes_recv)
                speed = ("{:.3f}".format(i_s))
                st_dw_speed= ("{:.2f}".format(st_dw))
                st_up_speed= ("{:.2f}".format(st_up))
                speak(f"Your internet speed is: {speed} MB per second, and\n upload speed is: {st_up_speed} MB per second\n download speed is: {st_dw_speed} MB per second")
            except Exception as e:
                speak("Cant access the internet speed right now please say it again..")
         
#--------------IP address----------#
        elif 'ip address' in query or "IP address" in query:
            try:
                ip = get("https://api.ipify.org").text
                speak(f"Your IP address is: {ip}")
            except Exception as e: 
             speak("Say that again please...")

#---------reminder-----------#      
        elif 'remember that' in query:
            try:
                rememberMsg = query.replace('remember that',"")
                speak("i successfully remembered that"+rememberMsg)
                rmbr=open("text_files/reminder.txt","w")
                rmbr.write(rememberMsg)
                rmbr.close()
            except Exception as e: 
             speak("Say that again please...")
        
        elif "reminder" in query or "what do you remember" in query:
            try:
                rmbr = open("text_files/reminder.txt","r")
                speak("yes sir..You told me to remind that:"+rmbr.read())
            except Exception as e: 
             speak("Say that again please...")

#------Taking screenshots-------#
        elif "take screenshot" in query or "take a screenshot" in query:
            try:    
                speak("By what name do you want to save the screenshot?")
                name = takecommand().lower()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"Screenshot/{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")
            except Exception as e: 
             speak("Say that again please...")

        elif "show me the screenshot" in query:
                try:
                    speak("Which screen shot do you want to see?")
                    name = takecommand()
                    img = Image.open(f'Screenshot/{name}.png')
                    img.show(img)
                    speak("Here it is sir")
                    time.sleep(2)
                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")   

        elif "terminate screenshot" in query:
            speak("screenshot terminated..")
            os.system("pkill Preview")

#----------For reading any pdf----------------

        elif "read" in query or "book" in query:
            try:    
                from functions.pdfreader import pdfread
                pdfread()
            except Exception as e: 
             speak("Say that again please...")

#----------To set alarm--------------#      
            
        elif 'alarm' in query:
            try:
                speak("Please Enter the time to set the alarm")
                print("Time format: HR:MM AM/PM)")
                alrm = input("Please Enter the time: ")
                from functions import alarm
                alarm.alarm(alrm)
            except Exception as e: 
             speak("Say that again please...")    
            
#-------------to send email --------#  
       
        elif ('email'in query or 'mail' in query):
            try:
                from functions.sendmail import sendEmail 
                speak('Please enter the email of receiver:')
                to = input("Enter the email id of reciever: ")
                speak(f'what should I say?')
                content = takecommand().lower()
                sendEmail(to, content)
                speak(f"Email has been sent!!")       
            except Exception as e:
                
                speak("sorry sir. I am not able to send this email.. try once again.")

#------------------Timepass----------------_#

        elif 'who are you' in  query or 'tell me about yourself' in query or 'what can you do' in query:
            try:
                speak('My Name is JAIVA, A Virtual Assistant..Mr. Akshay Created me in python for performing some tasks by voice commands.I can do tasks like Opening Google, Play music, Open Youtube, Can tell current time. Oepening notes and texteditor for you,and also Open applications like whatsapp, Music Applications, tell weather reports tell news and many more.. i can search wikipidea for any information u ask for and can google anything..locate any place on maps etc just give me commands and i will give you the responce accodingly..')
            except Exception as e:
                    speak("sorry sir. pardon please..")

#----------Search anything------#            
        elif 'what is' in query or 'how' in query:
            try:
                url = "https://www.google.co.in/search?q=" +(str(query))+ "&oq="+(str(query))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU" 
                webbrowser.open_new(url)
                time.sleep(2)
                speak('Here is your answer')
                time.sleep(5)
            except Exception as e:
                speak('Sorry, I am unable to answer it. say it again')

#---------to stop from listening for a time period--------#
        elif "don't listen" in query or "stop listening" in query or "a break" in query or "take a nap" in query  or "wait" in query :
            try:
                speak("for how much time you want to stop me from listening commands")
                print('please give the time only in integer form for eg: 10, 20, 30, 40...100')
                a = int(takecommand())
                speak(f"Ok sir.., i am taking a nap for {a} seconds")
                time.sleep(a)
                speak("it was a nice sleep, The time is over sir, i am back to work")
            except Exception as e:
                speak("Plese say it once again!")    

#------------searching mode- ask anything---------#
        elif 'mode' in query or 'mod' in query:
            try:
                speak('searching mod turned on.. Please tell what can i do for you?')
                com = takecommand().lower()
                com1 = com.replace("tell me","")
                com1 = com.replace("the","")
                mr = 1
                how_to = search_wikihow(com1,mr)
                assert len(how_to)== 1
                how_to[0].print()
                speak(how_to[0].summary)
            except Exception as e:
                speak('could not switch to Searching mode...please say that again..')

        elif 'stop' in  query or 'quit' in  query or 'exit' in  query or 'offline' in  query:
            try:
                from datetime import datetime
                hour = datetime.now().hour
                if  (hour >= 18) and (hour < 24):
                    speak(f"Okay {user} Sir! Good Night, Have a nice sleep!")
                else:
                    speak(f"Okay {user} sir! Have a nice day! ")
                    quit()
                sys.exit()
            except Exception as e:
                speak("say that again.")
          
        elif 'thank you' in  query  or 'no' in query:
            try:
                speak('Welcome sir! , if you need help, Call me anytime')
                break
            except Exception as e:
                speak("sorry sir. say it again.")

        speak("is there any other task for me?")

#-------Main class--------#

if __name__ == "__main__":

# ---------->Password protection<---------#
    speak("Please Enter Your password to Run the program..!")
    try:
        for i in range (3):
            print("You have only 3 attempts please be carefull..")
            a= input("Enter Your Password Here: ")
            pw_file = open("text_files/Pass.txt","r")
            pw = pw_file.read()
            pw_file.close()
            if(a==pw):
                # print("Welcome sir! Say Wake up to start..")
                break
            elif (i==2 and a!=pw):
                exit()
            elif(a!=pw):
                speak("Password is incorrect! Try Once Again..")
    except Exception as e:
        speak('Try again..')


    # recognizer =cv2.face.LBPHFaceRecognizer_create() #LLocal Binary Pattern Histogram
    # recognizer.read("trainer/trainer.yml") #load trained model
    # cascadePath = "haarcascade_frontalface_default.xml" #cascade file path
    # faceCascade = cv2.CascadeClassifier(cascadePath)    #initializing haar cascde for object detection

    # font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type

    # id = 6     #no of perosons you want to recognize

    # names = ['','akki']  #names, leave first empty because counter starts from 0

    # cam = cv2.VideoCapture(0) #to remove warning

    # cam.set(3, 640)   #set video frame width
    # cam.set(4, 480)    #set video frame height


    # #define main window size to be recognized as a face

    # minW = 0.1*cam.get(3)
    # minH = 0.1*cam.get(4)



    # while True:
    #         ret, img = cam.read() # read the frame using the above created object
    #         if not ret:
    #             print("Can't receive frame. (stream end?). Exiting ...")
    #             break
    #         converted_image =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts input into grayscale image

    #         faces = faceCascade.detectMultiScale(
    #                 converted_image,
    #                 scaleFactor = 1.2,
    #                 minNeighbors = 5,
    #                 minSize = (int(minW), int(minH)), 
    #         )

    #         for(x,y,w,h) in faces:
    #             cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),2)     #used to draw a rectangle on any image


    #             id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

    #             #check if accuracy is less than 100 ==> 0 is perfect match

    #             if  (accuracy < 100):
    #                 # id = names[id]
    #                 accuracy = " {0}%".format(round(100 - accuracy))
    #                 taskexecution()
                    
    #             else:
    #                 id = "unknown"
    #                 accuracy  = " {0}".format(round(100-accuracy))

    #             cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255),2)
    #             cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0),1)

    #         cv2.imshow('camera', img)

    #         k= cv2.waitKey(10) & 0xff  #press 'ESC' for exiting video
    #         if k == 27:
    #             break
            
    # print("Thanks for Using this program, Have a good day...")
    # cam.release()
    # cv2.destroyAllWindows()

    taskexecution()







   
