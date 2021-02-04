import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pathlib
import sys
from youtubesearchpython import VideosSearch


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
engine.setProperty('rate',145)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
print('Loading your AI personal assistant - G One')

f=open('setup/setup.txt','r')
x=f.readline()
f.close()
if x=='0':
    x=str(pathlib.Path().absolute())+'\setup'
    sys.path.insert(1, x)
    speak('Installing necessary modules. Please wait...')
    #print('Instaliravanje potrebnih modula. Pričekajte...')
    import setup
    f=open('setup/setup.txt','w')
    f.write('1')
    f.close()
    import os, winshell
    from win32com.client import Dispatch
    desktop = winshell.desktop()
    path = os.path.join(desktop, "Python AI Assistant.lnk")
    target = r"{}\python ai.py".format(pathlib.Path().absolute())
    wDir = r"{}".format(pathlib.Path().absolute())
    icon = r"{}\python ai logo.ico".format(x)
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()
    
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        #print("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        #print("Good Afternoon!")
    else:
        speak("Good Evening")
        #print("Good Evening!")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        if pauza==0:
            print("Listening...")
        elif pauza==1 and status=='listening':
            print('Paused')
        r.adjust_for_ambient_noise(source)
        #audio=r.listen(source)
        audio=r.listen(source,  phrase_time_limit=3)
        try:
            statement=r.recognize_google(audio,language='en-US')
            print(f"User said: {statement}\n")

        except Exception as e:
            if pauza==0:
                dad=0
                speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant G-One")
wishMe()
speak("Tell me how can I help you?")
pauza=0
warn=0
status='listening'

if __name__=='__main__':


    while True:
        statement = takeCommand().lower()
        if statement==0:
            continue
        if 'pause' in statement and pauza==0:
            speak('Pausing')
            pauza=1
            status='paused'
        if 'continue' in statement:
            speak('Listening')
            pauza=0
        if pauza==0:
            if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
                speak('your personal assistant G-one is shutting down. Good bye')
                break

            if 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                
            if 'youtube video' in statement:
                speak('What is the desired term you want to search for?')
                query=takeCommand()
                speak('Searching...')
                videosSearch = VideosSearch(query, limit = 1)
                x=str(videosSearch.result())
                y=x[x.find('https://www.youtube.com/watch?v='):
                    x.find('https://www.youtube.com/watch?v=')+43]
                print(y)
                webbrowser.open_new_tab(y)
                
            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(5)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                time.sleep(5)

            elif "weather" in statement:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name=takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature is " +
                          str(int(current_temperature)-273) + 'degrees celsius'
                          "\n humidity is " +
                          str(current_humidiy) +'percent'
                          "\n with " +
                          str(weather_description))
                    print(" Temperature: " +
                          str(int(current_temperature)-273)+' C°' +
                          "\n Humidity: " +
                          str(current_humidiy) +'%'
                          "\n Description: " +
                          str(weather_description))

                else:
                    speak(" City Not Found ")
                time.sleep(5)


            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'who are you' in statement or 'what can you do' in statement:
                speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                      'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                      'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by Mirthula and modified by Master Helix")
                print("I was built by Mirthula and modified by Master Helix")

            elif "open stackoverflow" in statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                speak("Here is stackoverflow")

            elif 'news' in statement:
                news = webbrowser.open_new_tab("https://www.24sata.hr/")
                speak('Here are some headlines from the twenty four hours. Happy reading')
                time.sleep(6)

            elif "camera" in statement or "take a photo" in statement:
                ec.capture(0,"robo camera","img.jpg")

            elif 'search'  in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(statement)
                time.sleep(5)

            elif 'ask' in statement:
                speak('I can answer to computational and geographical questions and what question do you want to ask now')
                question=takeCommand()
                app_id="R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)


            elif "log off" in statement or "sign out" in statement:
                speak('Are you sure you want to log off of your computer?')
                warn=1
            if 'yes' in statement and warn==1:
                warn=2
            if 'no' in statement and warn==1:
                warn=0
            if warn==2:
                warn=0
                speak("Ok. Your pc will log off in 10 seconds. make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
                
            elif 'restart' in statement:
                speak('Restarting')
                os.startfile('python ai.py')

time.sleep(3)
