import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def translator_action():
    subprocess.Popen(["python", "translator2.py"])

def talk_action():
    subprocess.Popen(["python", "speak.py"])

root = tk.Tk()
root.title("Merged Images")
root.geometry("800x440")  
root.configure(background='black')

# Load the images
trans_img = Image.open("trans.jpg")
speech_img = Image.open("speech.jpeg")

# Resize images to fit into the frame
trans_img = trans_img.resize((300, 300))
speech_img = speech_img.resize((300, 300))

# Convert images to Tkinter PhotoImage objects
trans_photo = ImageTk.PhotoImage(trans_img)
speech_photo = ImageTk.PhotoImage(speech_img)

# Create a frame to display the images and buttons
frame = tk.Frame(root, background='black')
frame.pack(pady=20)

# Display the images in labels
trans_label = tk.Label(frame, image=trans_photo)
trans_label.grid(row=0, column=0, padx=10)

speech_label = tk.Label(frame, image=speech_photo)
speech_label.grid(row=0, column=1, padx=10)

# Add a label above the images
title_label = tk.Label(root, text="TransVocal", font=("Arial", 20), fg="white", bg="black")
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Buttons
translator_btn = tk.Button(frame, text="Translator", font=("Arial", 12), command=translator_action)
translator_btn.grid(row=1, column=0, pady=10)

talk_btn = tk.Button(frame, text="Text to Speech", font=("Arial", 12), command=talk_action)
talk_btn.grid(row=1, column=1, pady=10)

root.mainloop()
