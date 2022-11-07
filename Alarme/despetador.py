from pygame import mixer
from datetime import datetime
from threading import Thread
from tkinter import *
from time import sleep

class Toque():
    def __init__(self, music, hour, minute, day):
        self.verify = True
        self.music = music
        self.hour = int(hour)
        self.minute = int(minute)
        self.day = day
        
        t1 = Thread(target=self.set_alarm)
        t1.start()
        
        mixer.init()
        
    def tocar(self):
        
        mixer.music.load(self.music)
        mixer.music.play()
        
    def stop(self):
        self.verify = False
        
    def set_alarm(self):
        count = 0
        while True:
            if(self.verify == True):
                now = datetime.now()
                hour_now = now.hour
                minute_now = now.minute
                day = int(now.strftime('%w'))
                
                print(minute_now,  self.minute, day, self.day)
                if(int(hour_now) == self.hour and int(minute_now) == self.minute and day == self.day):
                    self.tocar()
                    count += 1
                    if count == 3:
                        break
                sleep(1)
            else:
                break
