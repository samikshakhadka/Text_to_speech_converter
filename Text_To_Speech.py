from tkinter import *
from gtts import gTTS
from playsound import playsound

# initializing window
root = Tk()
root.geometry("350x300")
root.resizable(0,0)
root.configure(bg="ghost white")
root.title("TEXT TO SPEECH")

#heading and bottom part
Label(root, text="Text To Speech", font="arial 20 bold", bg="white smoke").pack()
Label(root, text="Samiksha", font="arial 10 bold", bg="white smoke", width='20').pack(side='bottom')

#enter text to be converted into speech
Label(root, text="Enter Text Here", font='arial 15 bold', bg= "white smoke").place(x=20,y=60)

#text var
msg= StringVar()


#entry
entry_field= Entry(root, textvariable=msg, width="50")
entry_field.place(x=20, y=100)

#function to convert text to speech
def text_to_speech():
    message= entry_field.get() 
    speech = gTTS(text=message)
    speech.save("audio.mp3")
    playsound('audio.mp3')


#function to exit
def Exit():
    root.destroy()

#Function to reset
def Reset():
    msg.set("")


#Define buttons
Button(root, text= "PLAY",font="arial 15 bold", command= text_to_speech, width= "4").place(x=25,y=140)

Button(root, font="arial 15 bold", text="EXIT", width="4", command=Exit, bg="Red").place(x=100, y=140)

Button(root, font="arial 15 bold", text="RESET", width='6', command= Reset).place(x=175, y=140)


#infinite loop
root.mainloop()