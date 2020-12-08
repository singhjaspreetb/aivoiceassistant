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
        
#this is first speak
engine = pyttsx3.init()
engine.say("Hi I am your voice assistant")
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
                        elif MyText == "what is artificial intelligence":
                            webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Artificial_intelligence")
                            engine = pyttsx3.init()
                            engine.say("Done")
                            engine.runAndWait()
                        elif MyText=="open google":
                                webbrowser.open_new_tab("http://www.google.com")
                                engine = pyttsx3.init()
                                engine.say("Done")
                                engine.runAndWait()
                        elif MyText == "open gmail":
                            webbrowser.open_new_tab("http://www.gmail.com")
                            engine = pyttsx3.init()
                            engine.say("Done")
                            engine.runAndWait()
                        elif MyText == "open youtube":
                            webbrowser.open_new_tab("http://www.youtube.com")
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
        
