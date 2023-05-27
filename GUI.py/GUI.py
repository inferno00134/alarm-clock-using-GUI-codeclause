import tkinter as tk
import datetime
import winsound

def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_hour = int(alarm_time[:2])
        alarm_minute = int(alarm_time[3:])
        now = datetime.datetime.now()
        alarm = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
        time_difference = alarm - now
        if time_difference.total_seconds() < 0:
            alarm = alarm.replace(day=alarm.day + 1)
        time_difference = alarm - now
        status_label.config(text=f"Alarm set for {alarm_time}")
        root.after(int(time_difference.total_seconds() * 1000), play_alarm)
    except ValueError:
        status_label.config(text="Invalid time format!")

def play_alarm():
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
    status_label.config(text="Wake up!")

root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Enter alarm time (HH:MM):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
