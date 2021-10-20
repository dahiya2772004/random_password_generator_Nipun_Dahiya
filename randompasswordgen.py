from tkinter import *

import random

import datetime

from gtts import gTTS

import os

def sub_pass_ran():

    lower="abcdefghijklmnopqrstwxyz"

    upper="ABCDEFGHIJKLMNOPQRSTWXYZ"

    numbers="0123456789"

    symbols="@#%^&*+="

    length=8

    all=lower+upper+numbers+symbols

    password=' '.join(random.sample(all,length))

    genfor=from_entry.get()

    current_timestamp = datetime.datetime.now()



    printable=genfor+"-"+" "+"the password generated at "+" "+ str(current_timestamp) +" "+ "is" + "   "+" "+ (password)+ "\n"



    final_var.set(printable)

    password_file=open("randompassword.txt","a")

    password_file.write(printable)

    password_file.close()

    fh=open("randompassword.txt","r" )

    mytext=fh.read().replace("\n","")

    language ="en"

    output=gTTS(text=mytext,lang=language,slow=False)

    output.save("output.mp3")

    fh.close()

    os.system("output.mp3")



passgen=Tk()

passgen.geometry("900x900")

passgen.title("rock password generator")

passgen["bg"]="#ea1414"

t_label=Label(passgen,text="Rock password generator",font=('Verdana', 25, 'bold') ,bg="#ea1414")

t_label.grid(row=0,column=0,padx=20,pady=20)

f_label=Label(passgen,text=" generate password for ",font="Calibri 25 bold ",bg="#ea1414")

f_label.grid(row=2,column=0,padx=10,pady=10)

#from entry

from_entry=Entry(passgen, font=("Aerial 35"), width=25)

from_entry.grid(row=2,column=1,padx=10,pady=10)



sub_button=Button(passgen,text="click to generate password ",width=28,command=sub_pass_ran, font="Calibri 25")

sub_button.grid(row=3,column=0)

frame3=Frame(passgen,bg="#FFFF00")

frame3.grid(pady=60)

final_var = StringVar()

pass_l=Label(frame3, text = "password", font='Calibri 20 bold',padx=10,pady=10,bg="#FFFF00")

pass_l.grid(row=0,column=1)

all_label=Label(frame3,textvariable=final_var,padx=10,pady=10,bg="#FFFF00")

all_label.grid(row=1,column=1)

copy_label=Label(passgen,text="Nipun,Shitij and Ishaan",font=(11),padx=5,pady=5,fg="#e7f4f4", bg="#008000")

copy_label.grid(row=9,column=0)

passgen.mainloop()