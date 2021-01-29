from translate import Translator
from gtts import gTTS
import os
from playsound import playsound
from tkinter import*
import sqlite3
window=Tk()
window.title("traduction ")
window.geometry("700x200")
window.config(background="#5596A4")
def action():
    x1=entry_1.get()
    translator=Translator(from_lang="english",to_lang="arabic")
    result=translator.translate(x1)
    string_to_display=str(result)
    var_1.set(string_to_display)

def play_1():

    r=str(entry_1.get())
    audio = "r.mp3"
    language = "en"
    sp = gTTS(text=r, lang=language, slow=False)
    sp.save(audio)
    playsound(audio)
def play_2():

    v=str(entry_2.get())
    audio = "speech.mp3"
    language = "ar"
    sp = gTTS(text=v, lang=language, slow=False)
    sp.save(audio)
    playsound(audio)


var_1=StringVar()
label=Label(window,text="English :" ,bg='#5596A4',font=("Courier",20)).place(x=65,y=50)
button_1=Button(text="play1",font=("courier",10),command=play_1)
button_1.place(x=55,y=130)
button_2=Button(text="play",font=("courier",10),command=play_2)
button_2.place(x=430,y=130)

entry_1=Entry(window,font=22 ,bg="red")
entry_1.place(x=55,y=100)
entry_2=Entry(window,textvariable=var_1,font=22 ,bg="red")
entry_2.place(x=430,y=100)
label=Label(window,text=": العربية " ,bg='#5596A4',font=("Courier",20)).place(x=490,y=50)
label=Label(window,text="-----------------> " ,bg='#5596A4',font=("Courier",20)).place(x=200,y=50)
button=Button(text="traduire ",font=("Courier",14),bg="red",command=action).place(x=280,y=160)


window.mainloop()