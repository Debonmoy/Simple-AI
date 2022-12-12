 
''' 
THIS IS A VOICE ASSISTANT MADE BY DEBONMOY PAL

HER NAME IS RITA

VERY IMPORTANT :
TO STOP THE ASSISTANT PRESS "CTRL+C" ON YOUR KEYBOARD

N-O-T-E:
         THIS IS STILL THE BETA VERSION, THE RELEASE OF THE FINAL VERSION WILL TAKE TIME

'''


''' Importing the required modules  '''

import pyttsx3 as pyx3
import speech_recognition as sr
import datetime
import pytz
import wikipedia
import webbrowser
import os

# Printing the introductory lines

print ("                            Hello                          ")
print ("     This is the start of conversation with Rita            ")
print ("-------------------------------------------------------------")
print ("   To stop the assistant press Ctrl+C on your keyboard    ")
print ("=============================================================")


# Initialize the engine 
engine = pyx3.init() 

voices = engine.getProperty('voices')
# Use female voice 
engine.setProperty('voice', voices[1].id) 

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
chrome = webbrowser.get(chrome_path)
# Speaking function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Main part starts here

# Making the greetings function
def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morning sir!")
    elif hour >=12 and hour <18:
        speak("Good afternoon sir!")
    elif hour >18:
        speak("Good evening sir!")

    speak(' I am Rita, how may I help you')



# Takes command from the user
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400 
        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.15
        r.dynamic_energy_ratio = 1.5
        r.operation_timeout = None 
        r.phrase_threshold = 0.3  
        r.non_speaking_duration = 0.5  
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("Your input >>> ",query)

    except Exception :
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
# Calling the takeCommand() function within an infinite loop
# So that our AI goes on taking commands
    while True:
        query = takeCommand().lower()

    # Building the logic of the AI
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening Youtube...')
            chrome.open ("youtube.com")

        elif 'open instagram' in query:
            speak('Opening instagram...')
            chrome.open ("instagram.com")

        elif 'open google' in query:
            speak('Opening google...')
            chrome.open ("google.com")

        elif 'open github' in query:
            speak('Opening github...')
            chrome.open ("github.com")

        elif 'open spotify' in query:
            speak('Opening Spotify...')
            chrome.open("https://open.spotify.com/?_ga=2.109911430.263056293.1604316969-1804211074.1600681864")

        elif 'open zoom' in query:
            speak('Opening Zoom Cloud Meetings...')
            os.startfile("C:/Users/DEBONMOY PAL/AppData/Roaming/Zoom/bin/Zoom.exe")

        elif 'open meet' in query:
            speak("Please enter the meeting id sir")
            url = (input("Enter your meeting id here >>> "))
            speak('Opening Google Meet')
            ot = (f"https://meet.google.com/{url}")
            chrome.open(ot)

        elif 'date' in query:
            x = datetime.datetime.now()
            y = x.strftime("%d""%B""%Y")
            speak(y)

        elif 'day' in query:
            x = datetime.datetime.now()
            y = x.strftime("%A")
            speak("Sir its "+y)

        elif 'time' in query:
            x = datetime.datetime.now()
            y = x.strftime("%I"+":"+"%M"+" "+"%p")
            speak ("The time is "+y)

        elif 'shutdown' or 'shut down' in query:
            speak("Shutting down sir...")
            break

        