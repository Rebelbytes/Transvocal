import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = tk.Tk()
root.title("Text to Speech")
root.geometry("1000x550")
root.resizable(False, False)
root.configure(bg="#D8BFD8")  

engine = pyttsx3.init()

#Top Frame
Top_frame = Frame(root, bg="#800080", width=1000, height=70)  
Top_frame.pack(side=TOP, fill=X)

Label(Top_frame, text="TEXT TO SPEECH", font="arial 30 bold", bg="#800080", fg="#FFFFFF").pack(pady=10) 

#Text Area
text_area = Text(root, font="Roboto ", bg="#E6E6FA", relief=GROOVE, wrap=WORD)  
text_area.place(x=100, y=100, width=400, height=400)

#Labels
Label(root, text="VOICE", font="arial 15 bold", bg="#D8BFD8", fg="#800080").place(x=550, y=150)  
Label(root, text="SPEED", font="arial 15 bold", bg="#D8BFD8", fg="#800080").place(x=750, y=150)  

# Comboboxes
gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='readonly', width=10)
speed_combobox.place(x=750, y=200)
speed_combobox.set('Normal')

# Functions
def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoices():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoices()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoices()
        else:
            engine.setProperty('rate', 60)
            setvoices()


def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoices():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        path = filedialog.askdirectory()
        os.chdir(path)
        engine.save_to_file(text, 'text.mp3')
        engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoices()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoices()
        else:
            engine.setProperty('rate', 60)
            setvoices()


# Buttons
btn = Button(root, text="Speak", compound=LEFT, width=13, font="arial 14 bold", command=speaknow, bg="#800080", fg="#FFFFFF")  
btn.place(x=550, y=280)

save = Button(root, text="Download", compound=LEFT, width=13, font="arial 14 bold", command=download, bg="#800080", fg="#FFFFFF")  
save.place(x=750, y=280)

root.mainloop()


