import datetime
import os
import random
import sys
import speech_recognition
import pyttsx3
import webbrowser
import speedtest
import pygame
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread,QTimer, QTime,QDate,Qt
from PyQt5.QtWidgets import QMainWindow
from Calculatenumbers import Calc, WolfRamAlpha
from userdb import login_user,register_user
from Kaidoui import Ui_Dailog
class SpeechRecognizer(QThread):
    def __init__(self):
        super(SpeechRecognizer,self).__init__()
    def run(self):
        self.recognize_speech()
    def recognize_speech(self):
        r=speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=300
        audio = r.listen(source,0,4)
        try:
            print("Understanding...")
            query = r.recognize_google(audio,language='en-in')
            print(f"You Said: {query}\n")
            return query
        except Exception as e:
            print("Say That Again")
            return "None"
class TaskExecutor:
    def __init__(self,query):
        self.query = query
    
    def execute_task(self):
        if "Wake up" in self.query:
            self.greet_user()
        elif "go to sleep" in self.query:
            self.sleep()
        #you can add more tasks here.....
    def greet_user(self):
        hour= int(datetime.datetime.now().hour)
        if hour >=0 and hour<=12:
            self.speak("Good Morning, sir")
        elif hour> 12 and hour<=18:
            self.speak("Good Afternoon, sir")
        else:
            self.speak("Good Evening, sir")
    def speak(self,text):
        engine=pyttsx3.init("sapi5")
        voice=engine.getProperty("voices")
        engine.setProperty("Voice",voice[0].id)
        engine.setProperty("rate",170)
        engine.say(text)
        engine.runAndWait()
class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.ui=Ui_Dailog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_task)
        self.ui.pushButton.clicked.connect(self.close)
    def start_task(self):
        self.ui.movie=QtGui.QMovie("../../Downloads/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        speech_recognizer = SpeechRecognizer()
        speech_recognition.start()
        query = speech_recognizer.recognize_speech()
        task_executor = TaskExecutor(query)
        task_executor.execute_task()
    def personal_assistant(self):
        print("Welcome to the Presonal Assistant")
        while True:
            action =input("Do You want to (1)Register or (2) Login?")
            if action == '1':
                username=input("Enter username:")
                password=input("Enter password:")
                register_user(username,password)
            elif action =='2':
                username=input("Enter username:")
                password=input("Enter password:")
            if login_user(username,password):
                print("Accessing Personal Assistant features...")
                self.takeCommand()
                break
            else:
                print("Invalid option")
    def run(self):
        self.start_task()
    def speak(self,audio):
        engine=pyttsx3.init("sapi5")
        voice=engine.getProperty("voices")
        engine.setProperty("voice",voice[0].id)
        engine.setProperty("rate",170)
        engine.say(audio)
        engine.runAndWait()
    def takeCommand(self):
        r=speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening.....")
            r.pause_threshold=1
            r.energy_threshold=300
            audio=r.listen(source,0,4)
        try:
            print("Understanding...")
            query=r.recognize_google(audio,language='en-in')
            print(f"You Said:{query}\n")
        except Exception as e:
            print("Say that Again")
            return "None"
        return query
    def personal_assistant(self):
        print("Welcome to the Personal Assistant")
        while True:
            action = input("Do you want to (1) Register or (2) login?")
            if action=='1':
                username=input("Enter username:")
                password=input("Enter password:")
                register_user(username,password)
            elif action=='2':
                username=input("Enter username:")
                password=input("Enter password:")
            if login_user(username,password):
                print("Accessing Personal Assistant features...")
                break
            else:
                print("Invalid option")
    def start_task(self):
        self.ui.movie=QtGui.QMovie("../../Downloads/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        while True:
            query=self.takeCommand().lower()
            if "hello kaido" in query:
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<=12:
                    print("Kaido:Good Morning Sir , 🤖 Kaido at your service. Ready to conquer tasks, control devices, and maybe... take over the world?   Just kidding... 😎, how are you Sir")
                    self.speak("Good Morning Sir, Kaido at your service. Ready to conquer tasks, control devices, and maybe... take over the world?   Just kidding..., how are you Sir")
                elif hour>12 and hour<=18:
                    print("Kaido:Good Afternoon Sir , 🤖 Kaido at your service. Ready to conquer tasks, control devices, and maybe... take over the world?   Just kidding... 😎,how are you Sir")
                    self.speak("Good Afternoon Sir, Kaido at your service. Ready to conquer tasks, control devices, and maybe... take over the world?   Just kidding..., how are you Sir ")
                else:
                    print("Kaido:Good Evening Sir , 🤖 Kaido at your service. Ready to conquer tasks, control devices, and maybe... take over the world?   Just kidding... 😎,how are you Sir")
                    self.speak("Good Evening Sir, Kaido at your service. Ready to conquer tasks, control devices, and maybe... take over the world?   Just kidding... ,how are you Sir ")
            elif "i am fine"in query:
                print("Kaido: Glad to hear that! Sir 😊 Your vibe is as smooth as my code today. What can I do for you today?")
                self.speak("Glad to hear that! Sir, Your vibe is as smooth as my code today. What can I do for you today?")
            elif "how are you" in query:
                print("Kaido: Me? Oh, I'm just a bunch of codes and algorithms vibing in the digital world. 😎 But thanks for asking! By the way, I'm always here to make your life easier. What can i do for you today? ")
                self.speak("Me? Oh, I'm just a bunch of codes and algorithms vibing in the digital world.  But thanks for asking! By the way, I'm always here to make your life easier. What can i do for you today? ") 
            elif "take screenshot" in query:
                print("Kaido: Taking Screenshot of your current screen sir, saved as screenshot.jpg")
                self.speak("Taking Screenshot of your current screen sir, saved as screenshot.jpg")
                import pyautogui #pip install pyautogui
                im=pyautogui.screenshot()
                im.save("screenshot.jpg")
            elif"open youtube"in query:
                print("Opening youtube in your browser...")
                self.speak("Opening youtube in your browser...")
                from Searchnow import searchYoutube
                searchYoutube(query)   
            elif "check internet speed" in query:
                wifi=speedtest.Speedtest()
                upload_net=wifi.upload()/1048576
                download_net=wifi.download()/1048576
                print("Kaido: your Wifi download speed is ",download_net)
                self.speak(f"Wifi download speed is {download_net}")
                print("Kaido: your Wifi upload speed is ",upload_net)
                self.speak(f"wifi upload speed is {upload_net}")
            elif "calculate" in query:
                from Calculatenumbers import WolfRamAlpha
                from Calculatenumbers import Calc
                query=query.replace("calculate","")
                query=query.replace("Kaido","")
                Calc(query)
            elif"whatsapp"in query:
                from Whatsapp import sendMessage
                sendMessage("+91 9353123881", "Hello Mohan Raj! This is Kaido ,your AI assistant.", 15, 30)
            elif "Let's play game" in query:
                from Game import game_play
                game_play()
            elif "translate" in query:
                from Translator import translategl
                query = query.replace("Kaido","")
                query=query.replace("translate","")
                translategl(query)
            elif "ipl score" in query:
                from plyer import notification #pip install plyer
                import requests #pip install requests
                from bs4 import BeautifulSoup #pip install bs4
                url="https://www.cricbuzz.com/"
                page=requests.get(url)
                soup=BeautifulSoup(page.text,"html.parser")
                team1=soup.find_all(class_="cb-ovr-flo cd-hmscrg-tm-n")[0].get_text()
                team2=soup.find_all(class_="cb-ovr-flo cb-hmscrg-tm-nm")[1].get_text()
                team1_score=soup.find_all(class_="cb-ovrflo")[8].get_text()
                team2_score=soup.find_all(class_="cb-ovr-flo")[10].get_text()
                a=print(f"{team1}:{team1_score}")
                b=print(f"{team2}:{team2_score}")
                notification.notify(
                    title="IPL Score:",
                    message=f"{team1}:{team1_score}\n {team2}:{team2_score}",
                    timeout=15
                )
            elif "click my photo" in query:
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                self.speak("SMILE")
                pyautogui.press("enter")
            elif " i am tired"in query:
                self.speak("playing your favorite song, sir")
                a=(1,2,3)
                b=random.choice(a)
                if b==1:
                    webbrowser.open("https://youtu.be/Vds8ddYXYZY?si=SdXRhvS85gKqMx4Z")
                elif "pause"in query:
                    pyautogui.press("k")
                    self.speak("video paused")
                elif "play"in query:
                    pyautogui.press("k")
                    self.speak("video played") 
                elif "mute"in query:
                    pyautogui.press("m")
                    self.speak("video muted")
                elif "volume up"in query:
                    from keyboard import volumeup
                    self.speak("Turning Up ,sir")
                    volumeup()
                elif "volume down"in query:
                    from keyboard import volumedown
                    self.speak("Turning volume Down, sir")
                    volumedown()
            elif "open" in query:
                from dictapp import openappweb
                openappweb(query)
            elif"close"in query:
                from dictapp import closeappweb
                closeappweb(query)
            elif "Google"in query:
                from Searchnow import searchGoogle
                searchGoogle(query)
            elif"Wikipedia"in query:
                from Searchnow import searchWikipedia
                searchWikipedia(query)
            elif"News"in query:
                from NewsRead import latestnews
                latestnews()                
            elif"temperature"in query:
                url = "https://www.weather-forecast.com/locations/YourCityName/forecasts/latest"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temperature = data.find("span", class_="wob_t").text
                print("Current Temperature:", temperature)
            elif"weather" in query:
                search="temperature in delhi"
                url =f"https://www.google.com/search?q={search}"
                r=requests.get(url)
                data=BeautifulSoup(r.text,"html.parser")
                temp=data.find("div",class_="BNeawe").text
                self.speak(f"current{search} is {temp}")
            elif "the time" in query:
                strTime=datetime.datetime.now().strftime("%H:%M")
                self.speak(f"Sir, the time is {strTime}")
            elif "exit"in query:
                print("Kaido:going to sleep sir, you can call me at any time")
                self.speak("going to sleep sir, you can call me at any time")
                exit()
            elif"remember that"in query:
                rememberMessage=query.replace("Remember that","")
                rememberMessage=query.replace("Kaido","")
                self.speak("you told me to remember that"+rememberMessage)
                remember=open("Remember.txt","a")
                remember.write(rememberMessage)
                remember.close()
            elif"what do you remember "in query:
                remember=open("Remember.txt","r")
                self.speak("you told me to remember that "+remember.read())
            elif "thank you"in query:
                print("You're welcome, legend! 😎 Helping you is what I was coded for 💻. Let me hear if you got any other cool tasks for me to handle? 🚀")
                self.speak("You're welcome, legend!  Helping you is what I was coded for. let hear if you got any other cool tasks for me to handle? ")
            elif"shutdown system"in query:
                self.speak("are you sure you want to shutdown")
                shutdown=input("do you wish to shutdown your computer?(yes/no)")
                if shutdown == "yes":
                    os.system("shutdown / s / t 1")
                elif shutdown == "no":
                    break

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    kaido=Main()
    kaido.show()
    sys.exit(app.exec_())    

    