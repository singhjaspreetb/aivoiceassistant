# Python program to translate 
# speech to text and text to speech 

import webbrowser
import speech_recognition as sr 
import pyttsx3 
from datetime import datetime


# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech


def SpeakText(command):

        # Initialize the engine
        engine = pyttsx3.init('dummy')
        engine.say(command)
        engine.runAndWait()

# Function to convert text to speech 
def SpeakText(command): 
        
        # Initialize the engine 
        engine = pyttsx3.init('dummy') 
        engine.say(command) 
        engine.runAndWait() 
        

engine = pyttsx3.init()
engine.say("Hi I am JARVIS, your personal assistant")
engine.runAndWait()
# Loop infinitely for user to speak 
text_length=0
# It will going to continue run until it count the text length less than 20.
while(text_length < 80):

       # Exception handling to handle
       # exceptions at the runtime
        try:
                engine = pyttsx3.init()
                engine.say("How can i help you")
                engine.runAndWait()
                # use the microphone as source for input.
                with sr.Microphone() as source2:

                        # wait for a second to let the recognizer
                        # adjust the energy threshold based on
                        # the surrounding noise level
                        r.adjust_for_ambient_noise(source2, duration=0.2)

                        #listens for the user's input
                        audio2 = r.listen(source2)

                        # Using google to recognize audio
                        MyText = r.recognize_google(audio2)
                        MyText = MyText.lower()

                        print("Command: \n"+MyText)
                        SpeakText(MyText)
                        if MyText == "hai" or MyText == "hello":
                                engine = pyttsx3.init()
                                engine.say("hello")
                                engine.runAndWait()
                        elif MyText == "open google" or MyText == "google":
                                webbrowser.open_new_tab("http://www.google.com")
                                engine = pyttsx3.init()
                                engine.say("Done")
                                engine.runAndWait()
                        elif MyText == "your name" or MyText == "what is your name":

                                engine = pyttsx3.init()
                                engine.say("Hello, my name is Jarvis")
                                engine.runAndWait()
                        elif MyText == "play music" or MyText == "music":
                                webbrowser.open_new_tab("https://music.youtube.com/watch?v=HC3-gSNbx00&list=RDAMVMHC3-gSNbx00")
                                engine = pyttsx3.init()
                                engine.say("Here the music")
                                engine.runAndWait()
                        elif MyText == "open gmail" or MyText == "gmail":
                                webbrowser.open_new_tab("http://www.gmail.com")
                                engine = pyttsx3.init()
                                engine.say("Here your gmail account")
                                engine.runAndWait()
                        elif MyText == "tell me about yourself" or MyText == "who are you" or MyText == "about yourself":
                                engine = pyttsx3.init()
                                engine.say("I am JARVIS... version ..1 point O...I have been created by... J. V. S. D. Co-operation. Its Members are JASPREET...VISHAL....Sonu.....DHRUV.")
                                engine.runAndWait()
                        elif MyText == "open youtube" or MyText == "youtube":
                                webbrowser.open_new_tab("http://www.youtube.com")
                                engine = pyttsx3.init()
                                engine.say("opened youtube")
                                engine.runAndWait()
                        elif MyText == "artificial intelligence" or MyText == "what is artificial intelligence":
                                webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Artificial_intelligence")
                                engine = pyttsx3.init()
                                engine.say("Artificial Intelligence is Technique that mimics Human Behaviour.It is widely used today in every field.")
                                engine.runAndWait()
                        elif MyText == "deep learning" or MyText == "what is deep learning":
                                webbrowser.open_new_tab("https://www.forbes.com/sites/bernardmarr/2018/10/01/what-is-deep-learning-ai-a-simple-guide-with-8-practical-examples/?sh=2c6e82058d4b")
                                engine = pyttsx3.init()
                                engine.say("Deep learning is a subset of machine learning where artificial neural networks, algorithms inspired by the human brain, learn from large amounts of data..")
                                engine.runAndWait()
                        elif MyText == "open blackboard" or MyText == "blackboard":
                                webbrowser.open_new_tab("https://cuchd.blackboard.com/?new_loc=%2Fultra%2Fcourse")
                                engine = pyttsx3.init()
                                engine.say("Here's The Blackboard From Chandigarh University")
                                engine.runAndWait()
                        elif MyText == "open university portal":
                                webbrowser.open_new_tab("https://uims.cuchd.in/UIMS/Login.aspx")
                                engine = pyttsx3.init()
                                engine.say("Here's Your C U I M S account")
                                engine.runAndWait()
                        elif MyText == "current time":
                                now = datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                print("Current Time =", current_time)
                                engine = pyttsx3.init()
                                engine.say(current_time)
                                engine.runAndWait()
                        elif MyText == "stop" or MyText == "bye" or MyText == "no thanks" or MyText == "bye bye jarvis":
                                text_length = 90
                                engine = pyttsx3.init()
                                engine.say("OK,Bye have a good day")
                                engine.runAndWait()
        except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
                engine = pyttsx3.init()
                engine.say("Say something")
                engine.runAndWait()
