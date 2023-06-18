
        # elif "instagram profile" in query:
        #     speak("Please enter the user name: ")
        #     username = str(input(""))
        #     webbrowser.open(f"www.instagram.com/{username}")
        #     speak(f"sir, Here is the profile of the user {username}")
        #     time.sleep(5)
        #     speak("sir. would you like to save the profile picture of this account?")
        #     condition = takecommand().lower()
        #     if "yes" in condition:
        #         mod =instaloader.Instaloader()
        #         mod.download_profile(username, profile_pic_only= True)
        #         path = f"{os.getcwd()}\\{username}.jpg"
        #         img = ImageGrab.grabclipboard()
        #         img.save(path)
        #         speak("Sure Sir!")
        #         os.startfile(path)
        #         #print(path)
        #     else:
        #         pass