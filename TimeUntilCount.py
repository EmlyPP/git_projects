import tkinter as tk
from datetime import datetime


class TimeUntilCount:
    def __init__(self):
        self.start = datetime.now()
        # self.stop = datetime(2025, 10, 26, 18, 35)
        u_year = int(input('Write your date:\n'
                           'Year: '))
        u_month = int(input('Month: '))
        u_day = int(input('Day: '))
        u_hour = int(input('Hour: '))
        u_minutes = int(input('Minutes: '))
        self.stop = datetime(u_year, u_month, u_day, u_hour, u_minutes)  # users input

        time_left = self.stop - self.start
        if 0 < time_left.days:
            tl_delta = str(str(time_left).split('.')[0])
        else:
            tl_delta = str('0 days,' + str(time_left).split('.')[0])
        tl_delta = tl_delta.replace(' days', '').replace(':', ',').replace(' ', '')
        tl_delta = list(str(tl_delta).split(','))
        if time_left.days == 0:
            days = 0
        else:
            days = tl_delta[0]
        self.days = int(days)  # start counting days
        self.hours = int(tl_delta[1])  # start counting hours
        self.minutes = int(tl_delta[2])  # start counting minutes
        self.seconds = int(tl_delta[3])  # start counting seconds
        # to add years
        self.label = tk.Label(win, text=f'{self.days} days {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}',
                              font="Lato 30", width=20)
        self.label.pack()
        self.label.after(1000, self.countdown_label)

    def countdown_label(self):

        if self.days <= 0 and self.hours <= 0 and self.minutes <= 0 and self.seconds <= 0:
            self.days = 0
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif self.hours == 0 and self.minutes == 0 and self.seconds == 0:
            self.days -= 1
            self.hours = 23
            self.minutes = 59
            self.seconds = 59
        elif self.minutes == 0 and self.seconds == 0:
            self.hours -= 1
            self.minutes = 59
            self.seconds = 59
        elif self.seconds == 0:
            self.minutes -= 1
            self.seconds = 59
        else:
            self.seconds -= 1

        self.label.configure(text=f"{self.days} days {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}", width=20)

        self.label.after(1000, self.countdown_label)


win = tk.Tk()
win.title("Time until")
win.attributes('-topmost', 1)
timer = TimeUntilCount()
win.mainloop()
