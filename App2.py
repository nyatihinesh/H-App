from tkinter import Tk,Button,Label,Text,END,RIDGE,NSEW,NW,Entry,Menu,Scrollbar,StringVar,OptionMenu,Frame, Toplevel,messagebox
from tkinter import filedialog,messagebox,colorchooser,simpledialog
from textblob import TextBlob
from plyer import notification
import numpy as np,wikipedia,sqlite3,time,cv2 as cv,csv
from textblob.translate import Translator
from PIL import Image, ImageTk
from pytube import YouTube
from math import *
import cvzone
from cvzone.HandTrackingModule import HandDetector
import random
from random import randint
from os import listdir
import speech_recognition as sr,pywhatkit
from gtts import gTTS
from datetime import datetime
from pyttsx3 import init
from statistics import mean,median,mode
from pygame import mixer
import pygame
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

mixer.init()

psa=0   
psb=0
csa=0
csb=0
name_to_greet = None

notification.notify(
    title="H-APP",message="Welcome to our app, hope you'll like it !!",timeout=10
)

def improvement():
    # Function To Ask For A Text Feedback And Ways To Improve
    root=Tk()
    root.config(bg="lightgreen")
    root.title("H-imp | Improvement")
    root.resizable(False,False)
    def submit():
        with open("feedback.txt",'w') as f:
            f.write(textbox.get(1.0,END))
    textbox=Text(root,borderwidth=9,relief=RIDGE,bg="yellow",fg="red",width=40,height=15,font=("comic sans ms",20))
    submitbtn=Button(root,text="Submit Feedback",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=20,command=submit,activebackground="yellow",activeforeground="green")
    textbox.grid(row=1,column=1)
    submitbtn.grid(row=2,column=1,columnspan=2)
    root.mainloop()
def feedback():
    # Creating A Function To Ask If The User Liked The App Via Messageboxes
    likedornot=messagebox.askyesno(title="LikeIt?",message="Did you like our app?")
    if likedornot==True:
        messagebox.showinfo(title="Thanks!",message="Thanks for your feedback, we request you to click on the improvement button on H-APP to tell us more!")
    else:
        messagebox.showinfo(title="Sorry!",message="Thanks for being honest,we request you to click on the improvement button on H-APP to tell us more as to what needs to be improved")
def calculator():
    # Creating A Function For A Simple Tkinter CalC With Limited Utilization
    
    root=Tk()
    root.title("H-calc | Calculator")
    root.config(bg="lightgreen")
    root.resizable(False,False)
    
    # Creating Functions To Operate And Evaluate The Question To Provide An Accurate Result
    def one():
        question.insert(END,"1")
    def two():
        question.insert(END,"2")
    def three():
        question.insert(END,"3")
    def four():
        question.insert(END,"4")
    def five():
        question.insert(END,"5")
    def six():
        question.insert(END,"6")
    def seven():
        question.insert(END,"7")
    def eight():
        question.insert(END,"8")
    def nine():
        question.insert(END,"9")
    def zero():
        question.insert(END,"0")
    def plus():
        question.insert(END,"+")
    def minus():
        question.insert(END,"-")
    def multiply():
        question.insert(END,"x")
    def divide():
        question.insert(END,"/")
    def opbrac():
        question.insert(END,"(")
    def clbrac():
        question.insert(END,")")
    def answer():
            try:
                realquestion=question.get()
                actualrealquestion=realquestion.replace("0","*")
                realanswer=round(eval(actualrealquestion),2)
                question.delete(0,END)
                question.insert(END,realanswer)
            except:
                pass
    def answerevent(event):
        try:
            realquestion=question.get()
            actualrealquestion=realquestion.replace("x","*")
            realanswer=round(eval(actualrealquestion),2)
            question.delete(0,END)
            question.insert(END,realanswer)
        except:
            question.delete(0,END)
    def clear():
        question.delete(0,END)
    def backspace():
        question.delete(len(question.get())-1,END)

    # Graphical User Interface For The CalC
    question=Entry(root, font=("Comic sans ms", 25), borderwidth=10,relief=RIDGE,bg="yellow",fg="red")
    bt1=Button(root,text="1",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=one)
    bt2=Button(root,text="2",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=two)
    bt3=Button(root,text="3",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=three)
    bt4=Button(root,text="+",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=plus)
    bt5=Button(root,text="4",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=four)
    bt6=Button(root,text="5",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=five)
    bt7=Button(root,text="6",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=six)
    bt8=Button(root,text="-",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=minus)
    bt9=Button(root,text="7",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=seven)
    bt10=Button(root,text="8",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=eight)
    bt11=Button(root,text="9",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=nine)
    bt12=Button(root,text="x",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=multiply)
    bt13=Button(root,text="(",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=opbrac)
    bt14=Button(root,text="0",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=zero)
    bt15=Button(root,text=")",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=clbrac)
    bt16=Button(root,text="/",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=divide)
    bt17=Button(root,text="C",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=clear)
    bt18=Button(root,text="|-",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=backspace)
    bt19=Button(root,text="Evaluate",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=12,activebackground="red",activeforeground="yellow",command=answer)

    question.grid(row=0,column=0,columnspan=4)
    bt1.grid(row=1,column=0)
    bt2.grid(row=1,column=1)
    bt3.grid(row=1,column=2)
    bt4.grid(row=1,column=3)
    bt5.grid(row=2,column=0)
    bt6.grid(row=2,column=1)
    bt7.grid(row=2,column=2)
    bt8.grid(row=2,column=3)
    bt9.grid(row=3,column=0)
    bt10.grid(row=3,column=1)
    bt11.grid(row=3,column=2)
    bt12.grid(row=3,column=3)
    bt13.grid(row=4,column=0)
    bt14.grid(row=4,column=1)
    bt15.grid(row=4,column=2)
    bt16.grid(row=4,column=3)
    bt17.grid(row=5,column=0)
    bt18.grid(row=5,column=1)
    bt19.grid(row=5,column=2,columnspan=2)

    # Binding The Enter Key Which Would Get The Answer, Rather Than Clicking The Button 
    root.bind("<Return>",answerevent)

    root.mainloop()
def notepad():
    # Creating A Funtion For A Notepad With Several Utilizations And Features Which Are Not Found In The Usual One
    
    root=Tk()
    root.title("H-pad | Notepad")
    root.resizable(False,False)
    root.lift()
    # Variables To Be Used Globally (in the notepad function) With Internal Nested Functions
    name=None
    nameex=False

    textbox=Text(root,borderwidth=10,relief=RIDGE,height=15,width=60,undo=True,font=("comic sans ms",18))
    textbox.grid(row=0,column=0)
    
    # Creating Nested Functions To Provide Functionality To The Buttons
    def new():
        global nameex
        nameex=False
        textbox.delete(1.0,END)
    def save():
        global name
        global nameex
        try:
            with open(f"{name}",'w') as f:
                f.write(textbox.get(1.0,END))
                nameex=True
        except:
            name=filedialog.asksaveasfilename()
            with open(f"{name}",'w') as f:
                f.write(textbox.get(1.0,END))
                nameex=True
    def opena():
        global nameex
        global name
        name=filedialog.askopenfilename()
        with open(f"{name}",'r') as f:
            textbox.delete(1.0,END)
            textbox.insert(END,f.read())
            nameex=True
    def saveas():
        global name
        global nameex
        name=filedialog.asksaveasfilename()
        with open(f"{name}",'w') as f:
            f.write(textbox.get(1.0,END))
            nameex=True
    def clear():
        textbox.delete(1.0,END)
    def changebg():
        requiredcolor=colorchooser.askcolor(title="Color Chooser Dialog")
        textbox["bg"]=requiredcolor[1]
    def changefg():
        requiredcolor=colorchooser.askcolor(title="Color Chooser Dialog")
        textbox["fg"]=requiredcolor[1]
    def ncsatt():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            text=r.recognize_google(r.listen(source))
            textbox.insert(END,text)
    def nptts():
        engine=init()
        voices=engine.getProperty("voices")
        rate=engine.getProperty("rate")
        engine.setProperty("voice",voices[1].id)
        engine.setProperty("rate",104)
        engine.say(textbox.get(1.0,END))
        engine.runAndWait()
    def ncsaveit():
        titleofit=filedialog.asksaveasfilename()
        texttosave=gTTS(text=textbox.get(1.0,END),lang="en",slow='False')
        texttosave.save(f"{titleofit}.mp3")
        mixer.init()
        mixer.music.load(f"{titleofit}.mp3")
        mixer.music.play()
    def openaevent(event):
        global nameex
        global name
        name=filedialog.askopenfilename()
        with open(f"{name}",'r') as f:
            textbox.delete(1.0,END)
            textbox.insert(END,f.read())
            nameex=True
    
    # Graphical User Interface
    
    mainmenu=Menu(root)

    filetab=Menu(mainmenu,title="File",tearoff=0)
    filetab.add_command(label="New (Ctrl+n)",command=new)
    filetab.add_command(label="Save (Ctrl+s)",command=save)
    filetab.add_command(label="Save As (Ctrl+shift+s)",command=saveas)
    filetab.add_command(label="Open (Ctrl+o)",command=opena)

    formattab=Menu(mainmenu,title="Format",tearoff=0)
    formattab.add_command(label="Change Background Color",command=changebg)
    formattab.add_command(label="Change Foreground Color",command=changefg)  

    texttospeechtab=Menu(mainmenu,title="Text and Speech",tearoff=0)
    texttospeechtab.add_command(label="Text to Speech",command=nptts)  
    texttospeechtab.add_command(label="Save TTS",command=ncsaveit)  
    texttospeechtab.add_command(label="Speech to Text",command=ncsatt)  

    mainmenu.add_cascade(menu=filetab,label="File")
    mainmenu.add_cascade(menu=formattab,label="Format")
    mainmenu.add_cascade(menu=texttospeechtab,label="Text and Speech")
    root.config(menu=mainmenu)

    scrollbar=Scrollbar(root,command=textbox.yview)
    scrollbar.grid(row=0,column=2,sticky=NSEW)
    textbox['yscrollcommand']=scrollbar.set
    
    # Binding Keys With Nested Functions For Easier Use
    root.bind("<Control-s>",save)
    root.bind("<Control-o>",openaevent)
    root.bind("<Control-n>",new)

    root.mainloop()
def wordcorrector():
    # Creating A Fuction To Get The Corrected Speeling Of A Misspelled Word
    
    root=Tk()
    root.title("H-word | Spelling Corrector")
    root.config(bg="lightgreen")
    root.resizable(False,False)

    # Creating The Required Main Nested Function
    def correctwordfn():
        try:
            correctwrd=TextBlob(misspelledword.get())
            correctedword.delete(0,END)
            correctedword.insert(END,correctwrd.correct())
        except:
            messagebox.showerror(title="Error!",message="An Unknown Error Occured")

    # Graphical User Interface
    
    Label(root,text="Misspelled word: ",font=("comic sans ms",15),bg="lightgreen",fg="red").grid(row=1,column=0)
    misspelledword=Entry(root,borderwidth=9,relief=RIDGE,bg="lightblue",fg="red",font=("comic sans ms",15),width=50)
    misspelledword.grid(row=1,column=1,sticky=NW)

    Label(root,text="Corrected word: ",font=("comic sans ms",15),bg="lightgreen",fg="red").grid(row=2,column=0)
    correctedword=Entry(root,borderwidth=9,relief=RIDGE,bg="lightblue",fg="red",font=("comic sans ms",15),width=50)
    correctedword.grid(row=2,column=1,sticky=NW)

    correctbtn=Button(root,text="Correct",borderwidth=9,relief=RIDGE,bg="yellow",fg="red",font=("comic sans ms",15),command=correctwordfn,activebackground="yellow",activeforeground="red").grid(row=3,column=0,columnspan=2)
    
    # Binding The Enter Key With The Main Nested Function For Easier Implementation
    root.bind("<Return>",correctwordfn)
    
    root.mainloop()    

def ytvi():
    filename=""
    def downloada():
        try:
            link=linkbox.get()
            path=locationbox.get()
            if link!="":
                if path!="":
                    ytvid=YouTube(link)
                    ytvid.streams.filter(progressive=True,file_extension="mp4").order_by('resolution').desc().first().download()
                    messagebox.showinfo(title="DONE!",message=f"The video has been successfully downloaded at {locationbox.get()}")
                    locationbox.delete(0,END)
                    linkbox.delete(0,END)
        except:
            messagebox.showerror(title="Error!",message='''Either one of the following errors occured:
                        1) Connection Error
                        2) Details filled aren't proper''')
    def detailsa():
        root=Tk()
        root.title("YT Video Details")
        root.geometry("1200x650")
        root.config(bg="yellow")
        
        def descr():
            
            link=linkbox.get()
            ytvid=YouTube(link)
            
            rooot=Tk()
            rooot.title("YT Video Description")
            rooot.geometry("1200x650")
            rooot.config(bg="yellow")
            
            labelol=Label(rooot, text=f'{ytvid.description}',bg="yellow",fg="red",font=("comic sans ms",10)).pack()
            
            rooot.mainloop()
        
        link=linkbox.get()
        ytvid=YouTube(link)
        
        titlea=ytvid.title
        legtha=ytvid.length
        viewsa=ytvid.views
        agea=ytvid.age_restricted
        channel=ytvid.channel_url
        thumbnail=ytvid.thumbnail_url
        
        labelol=Label(root, text=f''' Title: {titlea}\nLength: {legtha}\nViews: {viewsa}\nAge Restricted: {agea}\nChannel: {channel}\nThumbnail URL: {thumbnail}''',bg="yellow",fg="red",font=("comic sans ms",20)).pack()
        descriptionbtn=Button(root,text="Description",font=("comic sans ms",25),fg="red",bg="lightgreen",activeforeground="red",activebackground="lightgreen",borderwidth=9,relief=RIDGE,width=30,command=descr).pack()
        
        root.mainloop()
    def browsea():
        global filename
        filename=filedialog.askdirectory()
        locationbox.delete(0,END)
        locationbox.insert(END,filename)

    roota=Tk()
    roota.title("YT Guru")
    roota.geometry("1600x870")
    roota.config(bg="yellow")

    linkLabel=Label(roota, text="Link: ",bg="yellow",fg="red",font=("comic sans ms",35))
    locationLabel=Label(roota, text="Location: ",bg="yellow",fg="red",font=("comic sans ms",35))
    linkbox=Entry(roota,borderwidth=10,relief=RIDGE,bg="lightgreen",fg="red",font=("comic sans ms",25),width=35)
    locationbox=Entry(roota,borderwidth=10,relief=RIDGE,bg="lightgreen",fg="red",font=("comic sans ms",25),width=35)
    ytBrowse=Button(roota,text="Browse",font=("comic sans ms",30),fg="red",bg="lightgreen",activeforeground="red",activebackground="lightgreen",borderwidth=9,relief=RIDGE,width=30,command=browsea)
    ytDownload=Button(roota,text="Download",font=("comic sans ms",30),fg="red",bg="lightgreen",activeforeground="red",activebackground="lightgreen",borderwidth=9,relief=RIDGE,width=30,command=downloada)
    ytDetails=Button(roota,text="Details",font=("comic sans ms",30),fg="red",bg="lightgreen",activeforeground="red",activebackground="lightgreen",borderwidth=9,relief=RIDGE,width=30,command=detailsa)

    linkLabel.grid(row=0,column=0,pady=20,padx=20)
    linkbox.grid(row=0,column=1)
    locationLabel.grid(row=1,column=0,pady=20,padx=20)
    locationbox.grid(row=1,column=1)

    ytBrowse.grid(row=2,column=0,columnspan=2)
    ytDownload.grid(row=3,column=0,columnspan=2)
    ytDetails.grid(row=4,column=0,columnspan=2)

    roota.mainloop()
def dice():
    def simulate():
        randnum=randint(1,6)
        for i in range(1,7):
            if randnum==i:
                imagee=Image.open(f"DiceR/dice{i}.png")
                imageee=imagee.resize((300,300))
                mainImg=ImageTk.PhotoImage(imageee)
                diceLabel['image']=mainImg
                diceLabel.image=mainImg
                break
                
    rootzz=Tk()
    rootzz.title("Dice")
    rootzz.geometry("900x550")
    rootzz.config(bg="yellow")

    imagee=Image.open("DiceR/dice1.png")
    imageee=imagee.resize((300,300))
    mainImg=ImageTk.PhotoImage(imageee)

    diceLabel=Label(rootzz,image=mainImg,bg="yellow")
    diceLabel.image=mainImg
    diceSimulate=Button(rootzz,text="Simulate",command=simulate,font=("comic sans ms",30),fg="red",bg="lightgreen",activeforeground="red",activebackground="lightgreen",borderwidth=9,relief=RIDGE)

    diceLabel.pack(pady=20)
    diceSimulate.pack(pady=30)

    rootzz.mainloop()
def tth():
    def conv():
        nameOfFile=filedialog.asksaveasfilename()
        print(str(nameOfFile))
        pywhatkit.text_to_handwriting(str(textbox.get(1.0,END)),f"{str(nameOfFile)}.png")
        image1=Image.open(f"{str(nameOfFile)}.png")
        resized=image1.resize((1200,650))
        test = ImageTk.PhotoImage(resized)
        label1['image']=test
        label1.image=test
    root=Tk()
    root.title("Text to Handwriting")
    root.config(bg="yellow")

    textbox=Text(root,bg="lightgreen",fg="red",font=("comic sans ms",20),borderwidth=9,relief=RIDGE,height=5,width=70)
    mainbtn=Button(root,text="Save as Picture",bg="orange",fg="green",font=("comic sans ms",20),borderwidth=9,relief=RIDGE,command=conv)

    image1=Image.open("images/chrome.png")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test

    textbox.grid(row=0,column=0)
    mainbtn.grid(row=1,column=0)
    label1.grid(row=2,column=0)
    root.mainloop()
def tts():
    # Creating A Function To Convert Text To Speech In Various Voices, And Saving The Text
    root=Tk()
    root.resizable(False,False)
    root.title("H-tts | Text To Speech")
    root.config(bg="yellow")

    # Creating Functions For The Voices Of Ram, Lakshman And Sita Respectively
    def ram():
        try:
            titleoffile=filedialog.asksaveasfilename()
            words=gTTS(lang='en',text=text.get(1.0,END),slow=False)
            words.save(f"{titleoffile}.mp3")
            mixer.init()
            mixer.music.load(f"{titleoffile}.mp3")
            mixer.music.play()
        except:
            messagebox.showerror(title="Error!",message="An Unknown Error Occured")
    def lakshman():
        try:
            titleoffile=filedialog.asksaveasfilename()
            engine=init()
            voices=engine.getProperty("voices")
            engine.setProperty("voice",voices[0].id)
            engine.save_to_file(text=text.get(1.0,END),filename=f"{titleoffile}.mp3")
            engine.say(text.get(1.0,END))
            engine.runAndWait()
        except:
            messagebox.showerror(title="Error!",message="An Unknown Error Occured")
    def sita():
        try:
            titleoffile=filedialog.asksaveasfilename()
            engine=init()
            voices=engine.getProperty("voices")
            engine.setProperty("voice",voices[1].id)
            engine.save_to_file(text=text.get(1.0,END),filename=f"{titleoffile}.mp3")
            engine.say(text.get(1.0,END))
            engine.runAndWait()
        except:
            messagebox.showerror(title="Error!",message="An Unknown Error Occured")
        
    # Graphical User Interface
    
    text=Text(root,borderwidth=9,relief=RIDGE,font=("comic sans ms",15),height=15,width=40,bg="lightgreen",fg="red")
    firstoption=Button(root,text="Ram's Voice",borderwidth=9,relief=RIDGE,bg="lightblue",fg="green",font=("comic sans ms",15),width=15,command=ram,activebackground="lightblue",activeforeground="green")
    secondoption=Button(root,text="Lakshman's Voice",borderwidth=9,relief=RIDGE,bg="lightblue",fg="green",font=("comic sans ms",15),width=15,command=lakshman,activebackground="lightblue",activeforeground="green")
    thirdoption=Button(root,text="Sita's Voice",borderwidth=9,relief=RIDGE,bg="lightblue",fg="green",font=("comic sans ms",15),width=15,command=sita,activebackground="lightblue",activeforeground="green")

    text.grid(row=0,column=0,rowspan=30)
    firstoption.grid(row=0,column=1,sticky=NW)
    secondoption.grid(row=1,column=1,sticky=NW)
    thirdoption.grid(row=2,column=1,sticky=NW)

    root.mainloop()
def wiki():
  try:
    # Creating A Function For Browsing Wikipedia Pages And Getting Info from The Same
    root=Tk()
    root.config(bg="pink")
    root.title("H-info | Wikipedia")
    root.resizable(False,False)
    
    # Creating Nested Functions To Carry Out The Above
    def getDetail(event):
        det=wikipedia.summary(topic.get(),sentences=int(numberOfSentences.get()))
        detail.delete(1.0,END)
        detail.insert(END,det)
    def bolde(event):
        engine=init()
        voices=engine.getProperty("voices")
        engine.setProperty("voice",voices[1].id)
        engine.say(detail.get(1.0,END))
        engine.runAndWait()
    def bolkesavekr(event):
        titleoffile=filedialog.asksaveasfilename()
        sentences=gTTS(text=detail.get(1.0,END),lang='en',slow=False)
        sentences.save(f"{titleoffile}.mp3")
        mixer.init()
        mixer.music.load(f"{titleoffile}.mp3")
        mixer.music.play()
    
    # Graphical User Interface
    topic=Entry(root, borderwidth=10,relief=RIDGE,bg="yellow",fg="red",width=30,font=("comic sans ms", 20))
    numberOfSentences=Entry(root, borderwidth=10,relief=RIDGE,bg="red",fg="yellow",width=10,font=("comic sans ms", 20))
    detail=Text(root,borderwidth=10,relief=RIDGE,bg="lightgreen",fg="blue",width=79,height=20,font=("comic sans ms", 10))
    topic.grid(row=0,column=0)
    numberOfSentences.grid(row=0,column=1)
    detail.grid(row=1,column=0,columnspan=2,sticky=NSEW)
    
    # Binding Keyboard Keys To Run A Specific Function
    
    root.bind("<Control-s>",bolde)
    root.bind("<Control-l>",bolkesavekr)
    root.bind("<Return>",getDetail)
    
    root.mainloop()
  except:
    messagebox.showinfo("ERROR!","We're sorry but we couldn't find any information on this topic")
def statistics():
    
    # Creating A Function For Working Out The Statistical Data
    root=Tk()
    root.title("H-stat | Statistics")
    root.config(bg="lightgreen")
    root.resizable(False,False)
    
    data=[]
    dataentry=Entry(root,borderwidth=9,relief=RIDGE,bg="yellow",fg="red",font=("Comic sans ms",30),width="40")
    
    # Creating Various Nested Functions To Handle Statistical Mean, Median And Mode
    def one():
        dataentry.insert(END,"1")
    def two():
        dataentry.insert(END,"2")
    def three():
        dataentry.insert(END,"3")
    def four():
        dataentry.insert(END,"4")
    def five():
        dataentry.insert(END,"5")
    def six():
        dataentry.insert(END,"6")
    def seven():
        dataentry.insert(END,"7")
    def eight():
        dataentry.insert(END,"8")
    def nine():
        dataentry.insert(END,"9")
    def zero():
        dataentry.insert(END,"0")
    def add():
        data.append(int(dataentry.get()))
        dataentry.delete(0,END)
    def addevent(event):
        data.append(int(dataentry.get()))
        dataentry.delete(0,END)
    def meano():
        try:
            result["text"]= f'''The mean of 
            {data} is 
            {round(mean(int(n) for n in data),2)}'''
        except:
            result["text"]="An unknown error occured"
    def meanevent(event):
        try:
            result["text"]= f'''The mean of 
            {data} is 
            {round(mean(int(n) for n in data),2)}'''
        except:
            result["text"]="An unknown error occured"
    def mediano():
        try:
            result["text"]= f'''The median of 
            {data} is 
            {median(int(n) for n in data)}'''
        except:
            result["text"]="An unknown error occured"
    def medianevent(event):
        try:
            result["text"]= f'''The median of 
            {data} is 
            {median(int(n) for n in data)}'''
        except:
            result["text"]="An unknown error occured"
    def modeo():
        try:
            result["text"]= f'''The mode of 
            {data} is 
            {mode(int(n) for n in data)}'''
        except:
            result["text"]="Found two or more equally common values"
    def modeevent(event):
        try:
            result["text"]= f'''The mode of 
            {data} is 
            {mode(int(n) for n in data)}'''
        except:
            result["text"]="Found two or more equally common values"
    def restart():
        data.clear()
        result["text"]=""
    def restartevent(event):
        data.clear()
        result["text"]=""
    
    # Graphical User Interface
    bt1=Button(root,text="1",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=one,padx=5,pady=5)
    bt2=Button(root,text="2",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=two,padx=5,pady=5)
    bt3=Button(root,text="3",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=three,padx=5,pady=5)
    bt4=Button(root,text="4",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=four,padx=5,pady=5)
    bt5=Button(root,text="5",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=five,padx=5,pady=5)
    bt6=Button(root,text="6",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=six,padx=5,pady=5)
    bt7=Button(root,text="7",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=seven,padx=5,pady=5)
    bt8=Button(root,text="8",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=eight,padx=5,pady=5)
    bt9=Button(root,text="9",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=nine,padx=5,pady=5)
    bt10=Button(root,text="0",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,height=1,width=4,activebackground="red",activeforeground="yellow",command=zero,padx=5,pady=5)
    
    roo2=Frame(root)
    
    bt11=Button(roo2,text="Add",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,activebackground="red",activeforeground="yellow",command=add,padx=5,pady=5)
    bt12=Button(roo2,text="Mean",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,activebackground="red",activeforeground="yellow",command=meano,padx=5,pady=5)
    bt13=Button(roo2,text="Median",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,activebackground="red",activeforeground="yellow",command=mediano,padx=5,pady=5)
    bt14=Button(roo2,text="Mode",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,activebackground="red",activeforeground="yellow",command=modeo,padx=5,pady=5)
    bt15=Button(roo2,text="Restart",bg="red",fg="yellow",font=("comic sans ms",20),relief=RIDGE,borderwidth=10,activebackground="red",activeforeground="yellow",command=restart,padx=5,pady=5)
    result=Label(root,text="",bg="lightgreen",fg="red",font=("comic sans ms",25))
    dataentry.grid(row=0,column=0,columnspan=10)
    
    bt1.grid(row=1,column=0,sticky=NW)
    bt2.grid(row=1,column=1,sticky=NW)
    bt3.grid(row=1,column=2,sticky=NW)
    bt4.grid(row=1,column=3,sticky=NW)
    bt5.grid(row=1,column=4,sticky=NW)
    bt6.grid(row=1,column=5,sticky=NW)
    bt7.grid(row=1,column=6,sticky=NW)
    bt8.grid(row=1,column=7,sticky=NW)
    bt9.grid(row=1,column=8,sticky=NW)
    bt10.grid(row=1,column=9,sticky=NW)
    
    roo2.grid(row=2,column=0,columnspan=10)
    
    bt11.grid(row=0,column=0,sticky=NW)
    bt12.grid(row=0,column=1,sticky=NW)
    bt13.grid(row=0,column=2,sticky=NW)
    bt14.grid(row=0,column=4,sticky=NW)
    bt15.grid(row=0,column=6,sticky=NW)
    
    result.grid(row=3,column=0,columnspan=100,sticky=NW)
    
    # Binding Keyboard Keys With Functions For Easy Use
    root.bind("<Return>",addevent)
    root.bind("<Control-a>",meanevent)
    root.bind("<Control-b>",medianevent)
    root.bind("<Control-c>",modeevent)
    root.bind("<Control-d>",restartevent)
    
    root.mainloop()
def digi():
    # Creating A Function To Display The Live Time On The Mainroot Window
    global timern
    timerns=datetime.now().strftime("%H:%M:%S")
    timern['text']=timerns
    timern.after(1000,digi)
def db():
    
    # Creating A Function To Use Database Functions
    root=Tk()
    root.title("H-db | Database")
    root.config(bg="lightblue")
    root.resizable(False,False)

    def submit():
        conn=sqlite3.connect("school_book_3.db")
        c=conn.cursor()
        # c.execute("""
        #           CREATE TABLE detail (
        #               name text,
        #               classs text,
        #               rollno text
        #           );
        #           """)
        c.execute("INSERT INTO detail VALUES (:name, :classs,:rollno)",{'name':name.get(),
        'classs':classs.get(),
        'rollno':rollno.get()}
        )
        conn.commit()
        conn.close()
    def showrecords():
        conn=sqlite3.connect("school_book_3.db")
        c=conn.cursor()
        c.execute("SELECT*, oid FROM detail")
        records=c.fetchall()
        
        root1=Tk()
        root1.title("Database")
        root1.config(bg="lightblue")
        root1.resizable(False,False)
        name_records=''
        class_records=''
        rollno_records=''
        for record in records:
            name_records+=str(record[0]) + "\n"
            class_records+=str(record[1]) + "\n"
            rollno_records+=str(record[2]) + "\n"
        
        nametitle=Label(root1,text="Name",bg="lightblue",font=("comic sans ms",12)).grid(row=0,column=0)
        names=Label(root1,text=name_records,bg="lightblue",font=("comic sans ms",12)).grid(rowspan=100,column=0,row=1)
        classtitle=Label(root1,text="Class|Profession",bg="lightblue",font=("comic sans ms",12)).grid(row=0,column=1)
        classes=Label(root1,text=class_records,bg="lightblue",font=("comic sans ms",12)).grid(rowspan=100,column=1,row=1)
        rollnotitle=Label(root1,text="Roll No.",bg="lightblue",font=("comic sans ms",12)).grid(row=0,column=2)
        rollnos=Label(root1,text=rollno_records,bg="lightblue",font=("comic sans ms",12)).grid(rowspan=100,column=2,row=1)
        
        root1.mainloop()
        
        conn.commit()
        conn.close()

    # Graphical User Interface
    
    a=Label(root,text="Name: ",font=("comic sans ms",15),bg="lightblue")
    b=Label(root,text="Class: ",font=("comic sans ms",15),bg="lightblue")
    c=Label(root,text="Roll no.: ",font=("comic sans ms",15),bg="lightblue")

    name=Entry(root,width=30,font=("comic sans ms",15),borderwidth=5,relief=RIDGE,bg="yellow",fg="red")
    classs=Entry(root,width=30,font=("comic sans ms",15),borderwidth=5,relief=RIDGE,bg="yellow",fg="red")
    rollno=Entry(root,width=30,font=("comic sans ms",15),borderwidth=5,relief=RIDGE,bg="yellow",fg="red")

    submitbtn=Button(root,text="Add records to database",font=("comic sans ms",15),borderwidth=5,relief=RIDGE,bg="yellow",fg="red",activebackground="yellow",activeforeground="red",command=submit)
    showbtn=Button(root,text="Show database records",font=("comic sans ms",15),borderwidth=5,relief=RIDGE,bg="yellow",fg="red",activebackground="yellow",activeforeground="red",command=showrecords)

    a.grid(row=0,column=0,padx=20,pady=10)
    b.grid(row=1,column=0,padx=20,pady=10)
    c.grid(row=2,column=0,padx=20,pady=10)

    name.grid(row=0,column=1,padx=20,pady=10)
    classs.grid(row=1,column=1,padx=20,pady=10)
    rollno.grid(row=2,column=1,padx=20,pady=10)

    submitbtn.grid(row=3,column=0,columnspan=2)
    showbtn.grid(row=4,column=0,columnspan=2)

    root.mainloop()
def translator():
    root=Tk()
    root.title("H-tran | Translator")
    root.config(bg="lightblue")
    root.resizable(False,False)

    def transl():
        ds=Translator()
        sa=ds.translate(fromTranslation.get(1.0,END),from_lang=fromLang.get(),to_lang=toLang.get())
        toTranslation.delete(1.0,END)
        toTranslation.insert(END,sa)
        
    fromLang=StringVar(root)
    fromLang.set("Select A From_Language")
    toLang=StringVar(root)
    toLang.set("Select A To_Language")
    a=OptionMenu(root,fromLang,*["en","hi","zh","de","fr","es","it"])
    a.config(bg="yellow",fg="red",font=("comic sans ms",13),activebackground="yellow",activeforeground="red")
    a.grid(row=0,column=0)
    b=OptionMenu(root,toLang,*["en","hi","zh","de","fr","es","it"])
    b.config(bg="yellow",fg="red",font=("comic sans ms",13),activebackground="yellow",activeforeground="red")
    b.grid(row=0,column=2)
    Button(root,text="Translate",command=transl,bg="yellow",fg="red",activebackground="yellow",activeforeground="red",borderwidth=4,relief=RIDGE,font=("comic sans ms",13)).grid(row=0,column=1,padx=5,pady=5)

    fromTranslation=Text(root,borderwidth=10,relief=RIDGE,height=7,width=60,undo=True,font=("comic sans ms",18),bg="yellow",fg="red")
    fromTranslation.grid(row=1,column=0,columnspan=3,padx=5,pady=5)
    toTranslation=Text(root,borderwidth=10,relief=RIDGE,height=7,width=60,undo=True,font=("comic sans ms",18),bg="yellow",fg="red")
    toTranslation.grid(row=2,column=0,columnspan=3,padx=5,pady=5)

    root.mainloop()
def rps():
    # Creating A Function For A Rock Paper Scissors Game With A Graphical User Interface And AI Generated Results Using Messageboxes
    
    global csa,csb
    
    root=Tk()
    root.title("H-rps | Rock Paper Scissors")
    root.config(bg="yellow")
    root.resizable(False,False)
    
    # Creating Fuctions As To If The Player Chooses Rock, Paper Or Scissor, And Generating Computer's Random Choice via AI
    def rock():
        global csa,csb
        
        playerChoiceText="rock"
        compChoice=randint(1,3)
        
        if compChoice == 1:
            compChoiceText="rock"
        elif compChoice == 2:
            compChoiceText="paper"
        elif compChoice == 3:
            compChoiceText="scissor"
            
        if playerChoiceText == "rock":
            if compChoiceText=="rock":
                messagebox.showinfo("Its a tie !",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n The Rocks Collided")
            elif compChoiceText=="paper":
                messagebox.showinfo("You Lost...",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Computer's paper caught your rock !")
                csa += 0
                csb += 1            
                player["text"]=f"Player-{csa}"
                computer["text"]=f"Computer-{csb}"
            elif compChoiceText=="scissor":
                messagebox.showinfo("YOU WON !!",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Your Rock Hit Computer's Scissor and Broke It !")
                csa += 1
                csb += 0            
                player["text"]=f"Player-{csa}"
                computer["text"]=f"Computer-{csb}"
    def paper():
        global csa,csb
        
        playerChoiceText="paper"
        compChoice=randint(1,3)
        
        if compChoice == 1:
            compChoiceText="rock"
        elif compChoice == 2:
            compChoiceText="paper"
        elif compChoice == 3:
            compChoiceText="scissor"
            
        if playerChoiceText == "paper":
            if compChoiceText=="rock":
                messagebox.showinfo("YOU WON !!",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Your Paper Caught Computer's Rock !")
                csa += 1
                csb += 0            
                player["text"]=f"Player-{csa}"
                computer["text"]=f"Computer-{csb}"
            elif compChoiceText=="paper":
                messagebox.showinfo("Its a tie !",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n The Papers Collided")
            elif compChoiceText=="scissor":
                messagebox.showinfo("You Lost... !!",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Computer's Scissor Cuts Through Your Paper")
                csa += 0
                csb += 1            
                player["text"]=f"Player-{csa}"
                computer["text"]=f"Computer-{csb}"
    def scissor():
        global csa,csb
            
        playerChoiceText="scissor"
        compChoice=randint(1,3)
        
        if compChoice == 1:
            compChoiceText="rock"
        elif compChoice == 2:
            compChoiceText="paper"
        elif compChoice == 3:
            compChoiceText="scissor"
            
        if playerChoiceText == "scissor":
            if compChoiceText=="rock":
                messagebox.showinfo("You Lost... !!",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Computer's Rock Broke Your Scissor")
                csa += 0
                csb += 1
                player["text"]=f"Player-{csa}"
                computer["text"]=f"Computer-{csb}"
            elif compChoiceText=="paper":
                messagebox.showinfo("YOU WON !!",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Your Scissor Cut Through Computer's Paper !")
                csa += 1
                csb += 0            
                player["text"]=f"Player-{csa}"
                computer["text"]=f"Computer-{csb}"
            elif compChoiceText=="scissor":
                messagebox.showinfo("Its a tie !",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n The Scissors Collided")

    # Graphical User Interface
    
    Label(root,text="RPS",bg="yellow",fg="red",font=("comic sans ms",30),width=25).grid(row=0,column=0,columnspan=3)

    player=Label(root,text="Player-0",bg="yellow",fg="red",font=("comic sans ms",30))
    player.grid(row=1,column=0)
    winner=Label(root,text="",bg="yellow",fg="red",font=("comic sans ms",30))
    computer=Label(root,text="Computer-0",bg="yellow",fg="red",font=("comic sans ms",30))
    computer.grid(row=1,column=2)

    winner.grid(row=1,column=1)

    Button(root,text="Rock",bg="lightblue",fg="red",font=("comic sans ms",25),activebackground="lightblue",activeforeground="red",command=rock,borderwidth=9,relief=RIDGE,height=1,width=10).grid(row=2,column=0,padx=6,pady=6)
    Button(root,text="Paper",bg="lightblue",fg="red",font=("comic sans ms",25),activebackground="lightblue",activeforeground="red",command=paper,borderwidth=9,relief=RIDGE,height=1,width=10).grid(row=2,column=1,padx=6,pady=6)
    Button(root,text="Scissor",bg="lightblue",fg="red",font=("comic sans ms",25),activebackground="lightblue",activeforeground="red",command=scissor,borderwidth=9,relief=RIDGE,height=1,width=10).grid(row=2,column=2,padx=6,pady=6)

    root.call('wm', 'attributes', '.', '-topmost', '1')
    root.mainloop()
def swg():

    # Creating A Function For A Snake Water Gun Game With A Graphical User Interface And AI Generated Results Using Messageboxes
    
    global psa,psb
    
    root=Tk()
    root.title("H-swg | Snake Water Gun")
    root.config(bg="yellow")
    root.resizable(False,False)
    
    # Creating Fuctions As To If The Player Chooses Snake, Water Or Gun, And Generating Computer's Random Choice via AI
    def snake():
        global psa,psb
        
        playerChoiceText="snake"
        compChoice=randint(1,3)
        
        if compChoice == 1:
            compChoiceText="snake"
        elif compChoice == 2:
            compChoiceText="water"
        elif compChoice == 3:
            compChoiceText="gun"
            
        if playerChoiceText == "snake":
            if compChoiceText=="snake":
                messagebox.showinfo("Its a tie !",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n The Snakes Stung Each Other")
            elif compChoiceText=="water":
                messagebox.showinfo("YOU WON !!",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Your Snake Drunk Computer's Water !")
                psa += 1
                psb += 0            
                player["text"]=f"Player-{psa}"
                computer["text"]=f"Computer-{psb}"
            elif compChoiceText=="gun":
                messagebox.showinfo("You Lost...",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Computer's Gun Aimed, Shot And Killed Your Snake !")
                psa += 0
                psb += 1            
                player["text"]=f"Player-{psa}"
                computer["text"]=f"Computer-{psb}"
    def water():
        global psa,psb
        
        playerChoiceText="water"
        compChoice=randint(1,3)
        
        if compChoice == 1:
            compChoiceText="snake"
        elif compChoice == 2:
            compChoiceText="water"
        elif compChoice == 3:
            compChoiceText="gun"
            
        if playerChoiceText == "water":
            if compChoiceText=="snake":
                messagebox.showinfo("You Lost... !!",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Computer's Snake Drunk Your Water")
                psa += 0
                psb += 1            
                player["text"]=f"Player-{psa}"
                computer["text"]=f"Computer-{psb}"
            elif compChoiceText=="water":
                messagebox.showinfo("Its a tie !",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n The Water Got Mixed...")
            elif compChoiceText=="gun":
                messagebox.showinfo("YOU WON !!",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Your Water Got The Gun Drowned In It !")
                psa += 1
                psb += 0            
                player["text"]=f"Player-{psa}"
                computer["text"]=f"Computer-{psb}"
    def gun():
        global psa,psb
            
        playerChoiceText="gun"
        compChoice=randint(1,3)
        
        if compChoice == 1:
            compChoiceText="snake"
        elif compChoice == 2:
            compChoiceText="water"
        elif compChoice == 3:
            compChoiceText="gun"
            
        if playerChoiceText == "gun":
            if compChoiceText=="snake":
                messagebox.showinfo("YOU WON !!",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Your Gun Aimed, Shot And Killed Computer's Snake !")
                psa += 1
                psb += 0
                player["text"]=f"Player-{psa}"
                computer["text"]=f"Computer-{psb}"
            elif compChoiceText=="water":
                messagebox.showinfo("You Lost... !!",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n Your Gun Drowned Into Computer's Water")
                psa += 0
                psb += 1            
                player["text"]=f"Player-{psa}"
                computer["text"]=f"Computer-{psb}"
            elif compChoiceText=="gun":
                messagebox.showinfo("Its a tie !",f"You chose {playerChoiceText} \n Computer chose {compChoiceText} \n The Guns Shot Each Other")

    # Graphical User Interface
    
    Label(root,text="SWG",bg="yellow",fg="red",font=("comic sans ms",30),width=25).grid(row=0,column=0,columnspan=3)

    player=Label(root,text=f"Player-{psa}",bg="yellow",fg="red",font=("comic sans ms",30))
    player.grid(row=1,column=0)
    winner=Label(root,text="",bg="yellow",fg="red",font=("comic sans ms",30))
    computer=Label(root,text=f"Computer-{psb}",bg="yellow",fg="red",font=("comic sans ms",30))
    computer.grid(row=1,column=2)

    winner.grid(row=1,column=1)

    Button(root,text="Snake",bg="lightblue",fg="red",font=("comic sans ms",25),activebackground="lightblue",activeforeground="red",command=snake,borderwidth=9,relief=RIDGE,height=1,width=10).grid(row=2,column=0,padx=6,pady=6)
    Button(root,text="Water",bg="lightblue",fg="red",font=("comic sans ms",25),activebackground="lightblue",activeforeground="red",command=water,borderwidth=9,relief=RIDGE,height=1,width=10).grid(row=2,column=1,padx=6,pady=6)
    Button(root,text="Gun",bg="lightblue",fg="red",font=("comic sans ms",25),activebackground="lightblue",activeforeground="red",command=gun,borderwidth=9,relief=RIDGE,height=1,width=10).grid(row=2,column=2,padx=6,pady=6)

    root.call('wm', 'attributes', '.', '-topmost', '1')
    root.mainloop()
def fingerCounter():
    # OpenCV Function
    
    # Creating A Function Which Counts The Number Of Fingers Via A Deep Computer Vision Model and Displaying An Image Corresponding To The Fingers
    cap=cv.VideoCapture(0)
    detector=HandDetector(maxHands=1)
    folderPath="fingerImages"
    mylist=listdir(folderPath)
    overlaylist=[]
    for file in mylist:
        image=cv.imread(f"{folderPath}/{file}")
        overlaylist.append(image)
    text=None
    # While Loop Starts
    while True:
        success,img=cap.read()
        image=overlaylist[0]
        img=cv.flip(img,1)
        img=detector.findHands(img,False)
        lmlist=detector.findHands(img)
        cv.rectangle(img,(5,250),(205,450),(0,255,0),cv.FILLED)
        
        if len(lmlist) != 0:
            fingers=detector.fingersUp()
            totalFingers=fingers.count(1)
            if totalFingers == 0:
                image=overlaylist[5]
                text=0
            if totalFingers == 1:
                image=overlaylist[0]
                text=1
            if totalFingers == 2:
                image=overlaylist[1]
                text=2
            if totalFingers == 3:
                image=overlaylist[2]
                text=3
            if totalFingers == 4:
                image=overlaylist[3]
                text=4
            if totalFingers == 5:
                image=overlaylist[4]
                text=5
            cv.putText(img,str(text),(40,400),cv.FONT_HERSHEY_COMPLEX,5,(0,0,255),15)
            img[0:200,0:200]=image
            
        cv.imshow("Deep Computer Vision Finger Counter",img)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    cv.destroyAllWindows()

def ntfn():
    root=Tk()
    root.title("H-ntfn | Desktop Notifier")
    root.config(bg="lightblue")
    root.resizable(False,False)
    def notify():
        notification.notify(
            title=title.get(),message=message.get(),timeout=10
        )
        
    Label(root,text="Title: ",bg="lightblue",fg="red",font=("comic sans ms",20)).grid(row=0,column=0,padx=5,pady=5)
    Label(root,text="Message: ",bg="lightblue",fg="red",font=("comic sans ms",20)).grid(row=1,column=0,padx=5,pady=5)
    title=Entry(root,borderwidth=9,relief=RIDGE,bg="yellow",fg="red",font=("comic sans ms",20),width=20)
    message=Entry(root,borderwidth=9,relief=RIDGE,bg="yellow",fg="red",font=("comic sans ms",20),width=20)
    title.grid(row=0,column=1,padx=5,pady=5)
    message.grid(row=1,column=1,padx=5,pady=5)
    Button(root,text="Notify",bg="yellow",fg="red",font=("comic sans ms",20),command=notify,borderwidth=9,relief=RIDGE).grid(row=2,column=0,padx=5,pady=5,columnspan=2)

    root.mainloop()
def other():
    otherroot=Tk()
    otherroot.config(bg="lightgreen")
    otherroot.title("H-oth | Others")
    otherroot.resizable(False,False)   
    statisticsbtn=Button(otherroot,text="Statistics",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=10,command=statistics,activebackground="yellow",activeforeground="green")
    ttsbtn=Button(otherroot,text="TTS",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=10,command=tts,activebackground="yellow",activeforeground="green")
    infobtn=Button(otherroot,text="Wikipedia",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=10,command=wiki,activebackground="yellow",activeforeground="green")
    correctorbtn=Button(otherroot,text="Spell'd",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=10,command=wordcorrector,activebackground="yellow",activeforeground="green")
    dbbtn=Button(otherroot,text="DB",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=10,command=db,activebackground="yellow",activeforeground="green")
    rcsbtn=Button(otherroot,text="RPS",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=10,command=rps,activebackground="yellow",activeforeground="green")
    swgbtn=Button(otherroot,text="SWG",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=10,command=swg,activebackground="yellow",activeforeground="green")
    transbtn=Button(otherroot,text="Translator",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),command=translator,activebackground="yellow",activeforeground="green",width=10)
    notbtn=Button(otherroot,text="Notifier",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),command=ntfn,activebackground="yellow",activeforeground="green",width=10)
    tthbtn=Button(otherroot,text="TTH",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),command=tth,activebackground="yellow",activeforeground="green",width=10)
    dicebtn=Button(otherroot,text="Dice Roll",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),command=dice,activebackground="yellow",activeforeground="green",width=10)
    statisticsbtn.grid(row=0,column=0)
    ttsbtn.grid(row=0,column=1)
    infobtn.grid(row=0,column=2)
    correctorbtn.grid(row=1,column=0)
    dbbtn.grid(row=1,column=1)
    rcsbtn.grid(row=1,column=2)
    transbtn.grid(row=2,column=0)
    swgbtn.grid(row=2,column=1)
    notbtn.grid(row=2,column=2)
    # tthbtn.grid(row=3,column=0)
    # dicebtn.grid(row=3,column=1)
    otherroot.mainloop()

def askname():
    global name_to_greet
    root=Tk()
    root.title("What's Your Name ?")
    root.geometry("300x100")
    root.resizable(False,False)
    root.config(bg="lightblue")
    def ok():
        global name_to_greet
        if entrybtn.get() != "" :
            name_to_greet=entrybtn.get()
        else:
            messagebox.showwarning("Name?", "Kindly Enter Your Name, Before You Proceed.")
            askname()
        root.destroy()
    def ok2(event):
        global name_to_greet
        if entrybtn.get() != "" :
            name_to_greet=entrybtn.get()
        else:
            messagebox.showwarning("Name?", "Kindly Enter Your Name, Before You Proceed.")
            askname()
        root.destroy()
    entrybtn=Entry(root,font=("Comic Sans MS",15),borderwidth=10,relief=RIDGE,bg="red",fg="yellow")
    okbtn=Button(root,text="Ok",font=("Comic Sans MS", 15),command=ok,width=20,borderwidth=7,relief=RIDGE,bg="yellow",fg="red",activebackground="yellow",activeforeground="red")

    entrybtn.pack(padx=2,pady=2)
    okbtn.pack(padx=2,pady=2)

    root.bind("<Return>",ok2)
    root.mainloop()
def greetIt():
    global name_to_greet
    a=str(datetime.now())[11:13]
    print(a)
    if int(a) >= 4 and int(a) < 12:
        morning_message=gTTS(f"Good Morning, {name_to_greet}",lang='en',slow=False)
        morning_message.save(f"{name_to_greet}.mp3")
        mixer.init()
        mixer.music.load(f"{name_to_greet}.mp3")
        mixer.music.play()
    elif int(a) >= 12 and int(a) < 18:
        afternoon_message=gTTS(f"Good Afternoon, {name_to_greet}",lang='en',slow=False)
        afternoon_message.save(f"{name_to_greet}.mp3")
        mixer.init()
        mixer.music.load(f"{name_to_greet}.mp3")
        mixer.music.play()
    else:
        mixer.init()
        evening_message=gTTS(f"Welcome to Hinesh's App, {name_to_greet}",lang='en',slow=False)
        evening_message.save(f"{name_to_greet}.mp3")
        mixer.music.load(f"{name_to_greet}.mp3")
        mixer.music.play()

mainroot=Tk()
mainroot.title("H-APP | Hinesh's Application")
mainroot.config(bg="lightgreen")
mainroot.resizable(False,False)

title=Label(mainroot, text="Hinesh's App",bg="lightgreen",fg="red",font=("comic sans ms",40))
calcbtn=Button(mainroot,text="Calculator",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=10,command=calculator,activebackground="yellow",activeforeground="green")
notepadbtn=Button(mainroot,text="Notepad",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=10,command=notepad,activebackground="yellow",activeforeground="green")
ytvibtn=Button(mainroot,text="YTVI",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=10,command=ytvi,activebackground="yellow",activeforeground="green")
otherbtn=Button(mainroot,text="Other",borderwidth=9,relief=RIDGE,bg="yellow",fg="green",font=("comic sans ms",20),width=10,command=other,activebackground="yellow",activeforeground="green")
improvementbtn=Button(mainroot,text="Improvement",borderwidth=9,relief=RIDGE,bg="red",fg="yellow",font=("comic sans ms",20),width=14,command=improvement,activebackground="red",activeforeground="yellow")
feedbackbtn=Button(mainroot,text="Feedback",borderwidth=9,relief=RIDGE,bg="red",fg="yellow",font=("comic sans ms",20),width=10,command=feedback,activebackground="red",activeforeground="yellow")
timern=Label(mainroot,text="",font=("comic sans ms",60),bg="lightgreen",fg="red") 

title.grid(row=0,column=0,padx=10)
calcbtn.grid(row=1,column=0,pady=10,padx=10)
notepadbtn.grid(row=2,column=0,pady=10,padx=10)
ytvibtn.grid(row=3,column=0,pady=10,padx=10)
otherbtn.grid(row=4,column=0,pady=10,padx=10)
improvementbtn.grid(row=0,column=1,padx=40,pady=10)
feedbackbtn.grid(row=0,column=2,padx=25,pady=10)
timern.grid(row=2,column=1,columnspan=2)

mainroot.after(1,digi)
mainroot.mainloop()