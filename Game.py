import time
import datetime
import ctypes
import sys
import pyttsx3
import speech_recognition as sr
import random

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception:
        print("Say that again")
        return None
    return query

def game_play():
    print("Oh, I was born ready for this! Let's play stone paper scissor")
    speak("Oh, I was born ready for this! Let's play stone paper scissor")
    i = 0
    your_score = 0
    kaido_score = 0
    choices = ("stone", "paper", "scissors")

    while i < 5:
        kaido_choice = random.choice(choices)
        query = takeCommand()
        if query == "stone":
            if kaido_choice == "stone":
                speak("stone")
            elif kaido_choice == "paper":
                speak("PAPER")
                kaido_score += 1
            else:
                speak("SCISSORS")
                your_score += 1
        elif query == "paper":
            if kaido_choice == "stone":
                speak("stone")
                me_score += 1
            elif kaido_choice == "paper":
                speak("PAPER")
            else:
                speak("SCISSORS")
                kaido_score += 1
        elif query in ["scissor", "scissors"]:
            if kaido_choice == "rock":
                speak("ROCK")
                kaido_score += 1
            elif kaido_choice == "paper":
                speak("PAPER")
                your_score += 1
            else:
                speak("SCISSORS")
        i += 1
        print(f"Score: Me - {your_score}, Computer - {kaido_score}")

    print(f"Final Score: Me - {your_score}, Computer - {kaido_score}")

if is_admin():
    game_play()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def main():
    game_play()

if __name__ == '__main__':
    main()
