import time
import os

os.system("cls")


while True:
    minutes = input("Enter minutes: ")
    if minutes.isdigit():
        minutes_sec = int(minutes) * 60
        break
    else:
        print("Please enter a number.")

while True:
    seconds = input("Enter seconds: ")
    if seconds.isdigit():
        seconds_sec = int(seconds)
        break
    else:
        print("Please enter a number.")

total_time = minutes_sec + seconds_sec

while total_time >= 0:
        mins, secs = divmod(total_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        total_time -= 1
        time.sleep(1)






