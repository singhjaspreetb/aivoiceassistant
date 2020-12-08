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
        

engine = pyttsx3.init()
engine.say("Hi I am your assistant")
engine.runAndWait()
# Loop infinitely for user to speak 
text_length=0
# It will going to continue run until it count the text length less than 20.
while(text_length<80):   
   
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

                        print("Message: \n"+MyText) 
                        SpeakText(MyText) 
                        if MyText == "hai" or MyText == "hello":
                            engine = pyttsx3.init()
                            engine.say("hello")
                            engine.runAndWait()
                        elif MyText=="open google" or MyText=="google":
                                webbrowser.open_new_tab("http://www.google.com")
                                engine = pyttsx3.init()
                                engine.say("Done")
                                engine.runAndWait()
                        elif MyText=="play music" or MyText=="music":
                                 webbrowser.open_new_tab("https://www.jiosaavn.com/song/aankh-marey/BiQ9A0N9QXY")
                                 engine = pyttsx3.init()
                                 engine.say("Here the music")
                                 engine.runAndWait()
                        elif MyText == "open gmail" or MyText=="gmail":
                            webbrowser.open_new_tab("http://www.gmail.com")
                            engine = pyttsx3.init()
                            engine.say("Here your gmail account")
                            engine.runAndWait()
                        elif MyText == "open youtube" or MyText=="youtube":
                            webbrowser.open_new_tab("http://www.youtube.com")
                            engine = pyttsx3.init()
                            engine.say("opened youtube")
                            engine.runAndWait()
                        elif MyText == "artificial intelligence" or MyText=="what is artificial intelligence":
                            webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Artificial_intelligence")
                            engine = pyttsx3.init()
                            engine.say("Artificial Intelligence is Technique that mimics Human Behaviour.It is widely used today in every field.")
                            engine.runAndWait()
                        elif MyText == "open blackboard" or MyText=="blackboard":
                                webbrowser.open_new_tab("https://cuchd.blackboard.com/?new_loc=%2Fultra%2Fcourse")
                                engine = pyttsx3.init()
                                engine.say("Done")
                                engine.runAndWait()
                        elif MyText == "open university portal":
                                webbrowser.open_new_tab("https://uims.cuchd.in/UIMS/Login.aspx")
                                engine = pyttsx3.init()
                                engine.say("Done")
                                engine.runAndWait()
                        elif MyText == "current time":
                            now = datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            print("Current Time =", current_time)
                            engine = pyttsx3.init()
                            engine.say(current_time)
                            engine.runAndWait()
                        elif MyText=="stop":
                                text_length=90
                                engine = pyttsx3.init()
                                engine.say("Bye have a good day")
                                engine.runAndWait()
                        
        except sr.RequestError as e: 
                print("Could not request results; {0}".format(e)) 
                
        except sr.UnknownValueError: 
                print("unknown error occured")
        
