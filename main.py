
import sys
import pyaudiowpatch as pyaudio
sys.modules['pyaudio'] = pyaudio

import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import datetime

recognizer = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()



def processCommand(c):    

    command = c.lower()

    if"time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p") 
        speak(f"The time is {current_time}")

    elif"date" in command:
            current_date = datetime.datetime.now().strftime("%A, %B %d ,%Y") 
            speak(f"Today's date is {current_date}")    

    elif"open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif"open gmail" in command:
        speak("opening gmail")
        webbrowser.open("https://mail.google.com")    
 
   
    elif"open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif"open youtube" in command:
        speak("Opening Youtube")
        webbrowser.open("https://youtube.com")

    elif command.startswith("play"):

        song = c.lower().split(" ")[1]

        link = musiclibrary.music[song]

        webbrowser.open(link)    
    else:
        speak("Sorry,I dont know that command") 
     

if __name__== "__main__":

    speak("Initializing nova.....")

    while True:

        #Listen for the wake word "nova"
        #Obtail audio from the microphone
       
        
        try:

            with sr.Microphone() as source:
                
                print("Listening for wake word....")

                recognizer.adjust_for_ambient_noise(source, duration=0.5)

                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

                word = recognizer.recognize_google(audio)

            if "nova" in word.lower().strip():
               
                    print("1. Wake word detected")

                    print("2. Calling speak function")

                    speak("Yes, I am listening")

                                #Listen for command
                
            with sr.Microphone() as source:
                   
                    print("nova Active...")
                   
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5) 

                    command = recognizer.recognize_google(audio)

                    print("command:", command)

                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.WaitTimeoutError:
            print("Listening timed out.")  

        except sr.RequestError as e:
            print(f"Speech recognition API error: {e}")                 
        
        except Exception as e:  
            print(f"Error: {e}")



