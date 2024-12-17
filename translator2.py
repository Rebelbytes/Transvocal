import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator, utils

root = tk.Tk()
root.title("SK Translator 2.0")
root.geometry("1300x570")
root.resizable(False, False)
root.configure(background='#53868B')  

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c, bg='#104E8B', fg='#FFFFFF')  
    label2.configure(text=c1, bg='#104E8B', fg='#FFFFFF')  
    root.after(1000, label_change)

def translate_now():
    text_ = text1.get(1.0, END)
    try:
        translator = Translator()
        translation = translator.translate(text_, src=combo1.get(), dest=combo2.get())
        trans_text = translation.text
        print("Translated Text:", trans_text)  # Print translated text to console for debugging
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred during translation: {str(e)}")
        return

    text2.delete(1.0, END)
    text2.insert(END, trans_text)


# arrow
image_icon = PhotoImage(file="arrow.png")
image_label = Label(root, image=image_icon, width=150)
image_label.place(x=570, y=240)

language = googletrans.LANGUAGES
languageV = list(language.values())

# first combobox
combo1 = ttk.Combobox(root, value=languageV, font="Roboto 14", state="readonly", background='#104E8B', foreground='#030303')  
combo1.place(x=200, y=70)
combo1.set("ENGLISH")

label1 = Label(root, text="English", font="segoe 30 bold", bg='#FCE6C9', fg='#FCE6C9', width=18, bd=5, relief=GROOVE)
label1.place(x=100, y=130)

# second combobox
combo2 = ttk.Combobox(root, value=languageV, font="Roboto 14", state="readonly", background='#104E8B', foreground='#030303')  
combo2.place(x=850, y=70)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="English", font="segoe 30 bold", bg='#FCE6C9', fg='#FCE6C9', width=18, bd=5, relief=GROOVE)
label2.place(x=750, y=130)

# first frame
f = Frame(root, bg='#00688B', bd=5)  
f.place(x=100, y=200, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="#7AC5CD", fg="#000000", relief=GROOVE, wrap=WORD)  
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# second frame
f1 = Frame(root, bg='#00688B', bd=5)  
f1.place(x=750, y=200, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="#7AC5CD", fg="#000000", relief=GROOVE, wrap=WORD)  
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# translator button
translate = Button(root, text="Translate", font=("Roboto", 15), activebackground="#DED1B6", cursor="hand2",
                   bd=1, width=10, height=2, bg='#030303', fg='#FFFFFF', command=translate_now)  
translate.place(x=590, y=420)
label_change()

root.mainloop()

