import numpy as np
import cv2
from PIL import Image
import os

path ='samples'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def Image_And_Labels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    ids =[]

    for imagePath in imagePaths:
        gray_img = Image.open(imagePath).convert('L')
        img_arr =np.array(gray_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)

        for (x,y,w,h) in faces:
            faceSamples.append(img_arr[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids
print("Traning Faces. It will take Few Seconds. Please Wait...")

faces,ids = Image_And_Labels(path)
recognizer.train(faces, np.array(ids))

recognizer.write("trainer/trainer.yml")

print("Model Trained, Now We can recognize your face...")
