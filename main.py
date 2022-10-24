import tkinter
from tkinter import *
from gtts import gTTS
from playsound import playsound

window = Tk()
window.title('Text-To-Speech')
window.geometry('500x400')
window.resizable(0, 0)

heading = Label(window, text='  TEXT-TO-SPEECH  ', font='arial 20 bold', bg='light blue', relief=tkinter.RAISED,
                fg='black').pack(pady=10)

Msg = StringVar()
msg_label = Label(window, text='  Enter Your Text!😌  ', font='arial 20 bold', relief=tkinter.RIDGE, fg='black',
                  bg='ghost white').place(x=20, y=60)

entry_field = Entry(window,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save('Playtrack.mp3')
    playsound('Playtrack.mp3')

def Exit():
    window.destroy()

def Reset():
    Msg.set('')

Button(window, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)
Button(window, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)
Button(window, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

window.mainloop()
