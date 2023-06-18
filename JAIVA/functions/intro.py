from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time 


root= Tk()
root.geometry("700x400")



def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img 
    img = Image.open("gui/initial.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=1
    for img in ImageSequence.Iterator(img):
        img = img.resize((700,400))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.03)
    
    root.destroy()

play_gif()


root.mainloop()
