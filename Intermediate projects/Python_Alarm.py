from datetime import datetime
from playsound import playsound
alarm = input ("\nSET ALARM as - HH:MM:SS:AM/PM - format : \n")
a_hour = alarm[0:2]
a_minute = alarm[3:5]
a_second = alarm[6:8]
a_period = alarm[9:11].upper()
print("Alarm has been set \n")

while True:
 now = datetime.now()
 c_hour = now.strftime("%I")
 c_minute = now.strftime("%M")
 c_second = now.strftime("%S")
 c_period = now.strftime("%p")
 if (a_period == c_period):
    if (a_hour == c_hour):
        if (a_minute == c_minute):
            if (a_second == c_second):
                print("ITS TIME")
                playsound("Coffin_dance.mp3")
                break
            
                