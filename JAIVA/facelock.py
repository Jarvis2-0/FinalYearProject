import cv2


recognizer =cv2.face.LBPHFaceRecognizer_create() #LLocal Binary Pattern Histogram
recognizer.read("trainer/trainer.yml") #load trained model
cascadePath = "haarcascade_frontalface_default.xml" #cascade file path
faceCascade = cv2.CascadeClassifier(cascadePath)    #initializing haar cascde for object detection

font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type

id = 1      #no of perosons you want to recognize

names = ['','akki']  #names, leave first empty because counter starts from 0

cam = cv2.VideoCapture(0) #to remove warning

cam.set(3, 640)   #set video frame width
cam.set(4, 480)    #set video frame height


#define main window size to be recognized as a face

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)



while True:
        ret, img = cam.read() # read the frame using the above created object
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        converted_image =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts input into grayscale image

        faces = faceCascade.detectMultiScale(
                converted_image,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)), 
        )

        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),2)     #used to draw a rectangle on any image


            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

            #check if accuracy is less than 100 ==> 0 is perfect match

            if  (accuracy < 100):
                # name = names[id]
                accuracy = " {0}%".format(round(100 - accuracy))
                
            else:
                id = "unknown"
                accuracy  = " {0}".format(round(100-accuracy))

            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255),2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0),1)

        cv2.imshow('camera', img)

        k= cv2.waitKey(10) & 0xff  #press 'ESC' for exiting video
        if k == 27:
               break
        
print("Thanks for Using this program, Have a good day...")
cam.release()
cv2.destroyAllWindows()

        

 





























# import pickle
# import face_recognition as fr


# video_capture = cv2.VideoCapture(0)
# face_is_match = False
# face_encodings = []
# known_face_encodings = pickle.load(open('encode.pickle','rb'))
      
# while True:
#         ret, frame = video_capture.read()
#         face_locations = fr.face_locations(frame, model="hog")
#         face_encodings = fr.face_encodings(frame, face_locations)
               
#         face_names = []
#         name = "Unknown"
# for face_encoding in face_encodings:
#                 matches = fr.compare_faces(known_face_encodings, face_encoding, 0.4)
            
#                 #find first match
#                 if True in matches:
#                         first_known_face = matches.index(True)
#                         print("Welcome")
#                         face_is_match = True
                
#                 else:
#                         print("Access Denied")

