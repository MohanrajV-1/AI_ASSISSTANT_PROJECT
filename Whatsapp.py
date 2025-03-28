import pywhatkit
from datetime import datetime

def sendMessage(number, message,current_hour,current_minute):
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute + 1

    if current_minute >= 60:
        current_hour += 1
        current_minute -= 60

    pywhatkit.sendwhatmsg(number, message, current_hour, current_minute)
    print("Message scheduled successfully!")
