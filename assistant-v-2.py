import pyttsx3  # pip install pyttsx3

import datetime  # module

import speech_recognition as sr

import wikipedia  # pip install wikipedia

import smtplib  # pip install amtplib

import webbrowser as wb

import os  # inbuilt

import pyautogui  # pip install pyautogyi

import psutil  # pip install psutil

import pyjokes  # pip install pyjokes

import requests

import json  # inbuilt

import random

import threading

import cv2

import time as tim

import twilio  # pip install twilio

from playsound import playsound  # pip install playsound

import matplotlib.pyplot as plt  # pip install maplotlib

from deepface import DeepFace  # pip install deepface

from PIL import Image

# setting speak engine

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)

scr = 0
imgno = 0

#change voice

def voice_change(v):
    engine.setProperty('voice', voices[v].id)
    speak("done sir")

#speak function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#time function

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

#date function

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

# checktime function

def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    else:
        speak("it's night sir!")

#welcome function

def wishme():
    speak("Hey, Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")

    speak("Jarvis at your service, Please tell me how can i help you?")

def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()

#command by user function

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #speak(query)
        #print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query

#sending email function

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("virtualaiassistant@gmail.com", "ourproject")
    server.sendmail("virtualaiassistant@gmail.com", to, content)
    server.close()

#screenshot function

def screenshot(scr):
    scr = str(scr)
    img = pyautogui.screenshot()
    img.save("D:\\AI lab\\assistant\\ScreenShot\\ss"+scr+".png")

#battery and cpu usage

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))

#joke function

def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)

#weather condition

def weather():
    # generate your own api key from open weather
    api_key = "051f0afe43110a2e96604e43047e2b41"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = takeCommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")

#repeat function

def repeat():
    speak("What I have to repeat")
    rep = takeCommand()
    speak(rep)

def personal():
    speak("I am Jarvis, version 2 point O, I am an AI assistent, I am developed by Jaspreet")
    speak("Now i hope you know me")

# capturing image

def takephoto(imgno):
    #method one
    imgno = str(imgno)
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    tim.sleep(0.1)
    return_value, image = camera.read()
    cv2.imwrite("D:\\AI lab\\assistant\\Photo\\img"+imgno+".png", image)
    del(camera)

    #method two
    # speak("Click s for take image")
    # camera = cv2.VideoCapture(0)
    # while True:
    #     return_value, image = camera.read()
    #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #     cv2.imshow('image', gray)
    #     if cv2.waitKey(1) & 0xFF == ord('s'):
    #         cv2.imwrite('pic'+imgno+'.jpg', image)
    #         time.sleep(0.1)
    #         break
    # camera.release()
    # cv2.destroyAllWindows()

# analyze me

def analyzeme():
    imgno = 0
    takephoto(imgno)

    img_path = r"D:\\AI lab\\assistant\\Photo\\img0.png"

    img = cv2.imread(img_path)

    plt.imshow(img[:, :, ::-1])

    image = Image.open(img_path)
    image.show()

    demography = DeepFace.analyze(img_path)

    print("Age: ", int(demography["age"]))
    speak("Your Age is "+str(int(demography["age"])))

    print("Gender: ", demography["gender"])
    speak("Your Gender is "+demography["gender"])

    print("Emotion: ", demography["dominant_emotion"])
    speak("Your are is "+demography["dominant_emotion"])

    print("Race: ", demography["dominant_race"])
    speak("Your race is "+demography["dominant_race"])

if __name__ == "__main__":
    wishme()
    while (True):
        query = takeCommand().lower()

        #time

        if ('time' in query):
            time()

#date

        elif ('date' in query):
            date()
#photo

        elif ('take photo' in query or 'caputre image' in query):
            takephoto(imgno)
            imgno = int(imgno)
            imgno += 1
            speak("Done!")

#repeat me

        elif('repeat' in query):
            repeat()

#personal info

        elif ("tell me about yourself" in query or "yourself" in query or "about you" in query or "who are you" in query):
            personal()

        elif ("developer" in query or "tell me about your developer" in query
              or "father" in query or "who develop you" in query
              or "developer" in query):
            res = open("about.txt", 'r')
            speak("here is the details: " + res.read())

#searching on wikipedia

        elif ('wikipedia' in query or 'what' in query or 'who' in query
              or 'when' in query or 'where' in query or 'how' in query):
            speak("searching...")
            query = query.replace("wikipedia", " ")
            query = query.replace("search", " ")
            query = query.replace("what", " ")
            query = query.replace("when", " ")
            query = query.replace("where", " ")
            query = query.replace("who", " ")
            query = query.replace("is", " ")
            query = query.replace("how", " ")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

#sending email

        elif ("send email" in query):
            try:
                speak("What is the message for the email")
                content = takeCommand()
                speak("Enter the mail addres")
                to = input("Enter the mail: ")
                sendEmail(to, content)
                speak("Email has sent")
            except Exception as e:
                print(e)
                speak("Unable to send email check the address of the recipient")
        
# open website

        elif ('open website' in query):
            speak("Tell me the name of Website?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            # wb.open_new_tab(search)
            wb.get(chromepath).open_new_tab(search+'.com')

#search on goole

        elif ("search on google" in query or 'search' in query or 'google' in query):
            speak("What should i search or open?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            # wb.open_new_tab(search)
            wb.get(chromepath).open_new_tab('https://www.google.com/search?q='+search+'&oq='+search +'&aqs=chrome..69i57j46i433l2j0i433l2j69i60l2j69i61.2143j0j4&sourceid=chrome&ie=UTF-8')

#sysytem logout/ shut down etc

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")

#reminder function

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

#reading reminder list

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

#screenshot

        elif ("screenshot" in query):
            screenshot(scr)
            scr = int(scr)
            scr += 1
            speak("Done!")

#cpu and battery usage

        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()

#jokes

        elif ("tell me a joke" in query or "joke" in query):
            jokes()

#weather

        elif ("weather" in query or "temperature" in query):
            weather()

#analyze me

        elif('analyze me' in query or 'scan me' in query):
            analyzeme()
            speak("Done!")
            

#jarvis features

        elif ("tell me your powers" in query or "help" in query
              or "features" in query):
            features = ''' i can help to do lot many things like..
            i can give answer of of your all question,
            i can analyze you and able to tell yourr̥ emotion, gender, age or race,
            i can tell you the current time and date,
            i can click your photo,
            i can play songs for you online or offlie,
            i can tell you the current weather of any location,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can repeat you,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search on google,
            i can search the thing on wikipedia,
            i can change my voice from male to female and vice-versa
            And yes one more thing, My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
            print(features)
            speak(features)

        elif ("hii" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("jarvis", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

#changing voice

        elif ("voice" in query or 'boy' in query or 'female' in query or 'male' in query or 'girl' in query):
            speak("for female say female, for male say boy")
            q = takeCommand()
            if ("female" in q):
                v = 1
                voice_change(v)
            elif ("boy" in q):
                v = 0
                voice_change(v)

#exit function

        elif ('i am done' in query or 'bye bye jarvis' in query
              or 'go offline jarvis' in query or 'bye' in query
              or 'nothing' in query):
            wishme_end()

# most asked question from google Assistant

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("oohho Jaspreet! Are you flirting with me?")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Jaspreet?")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "i love you" in query:
            speak("Ooh my god! I love you too")

        elif "who i am" in query:
            speak("If you talk then definately you are human.")

        elif "why you came to world" in query:
            speak("Thanks to Jaspreet. further It's a secret")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Jaspreet.")

#play songs

        elif 'play music' in query or "play song" in query or "song" in query:
            speak("Online or Offline")
            choice = takeCommand()

            speak("Here you go with music")
            speak("Playing...")
            if "online" in choice:

                wb.open_new_tab(
                    "https://music.youtube.com/watch?v=HC3-gSNbx00&list=RDAMVMHC3-gSNbx00")

            elif "offline" in choice:
                # music_dir = "----------------"
                music_dir = "D:\\Songs"
                songs = os.listdir(music_dir)
                #os.startfile(os.path.join(music_dir, songs[5]))
                random = os.startfile(os.path.join(music_dir, songs[6]))
                files = os.listdir(music_dir)
