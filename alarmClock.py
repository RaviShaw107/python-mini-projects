from playsound import playsound    # module for playing audio files
from datetime import datetime     # module for working with dates and times

def setAlarm(alarmTime):
    while True:

        currentTime = datetime.now().strftime("%H:%M:%S")   # datetime.now()  =)  gets the current date and time.
                                                         # strftime("%H:%M:%S")  =)  converts the time into string format
        if alarmTime == currentTime:
            playsound("shankar.mp3")  # Replace "shankar.mp3" with the path to your alarm sound file
            print("Wake up! \n" * 5)
            break

def __main__():     # main() is a magic method
    currentTime = 0
    alarmTime = input("set alarm time in HH:MM:SS format (24-hour): \n")
    setAlarm(alarmTime)

__main__()