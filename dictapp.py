import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

# Dictionary moved outside the function for accessibility
dictapp = {
    "commandprompt": "cmd",
    "paint": "paint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt"
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("Kaido", "")
        query = query.replace("launch", "")
        webbrowser.open(f"https://www.{query}")
    else:
        for app in dictapp:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing, sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "2 tab" in query:
        for _ in range(2):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("All tabs closed")
    elif "3 tab" in query:
        for _ in range(3):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("All tabs closed")
    elif "4 tab" in query:
        for _ in range(4):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("All tabs closed")
    elif "5 tab" in query:
        for _ in range(5):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("All tabs closed")
    else:
        for app in dictapp:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
