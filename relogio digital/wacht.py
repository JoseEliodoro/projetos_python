import random
from tkinter import *
from datetime import datetime

import pyglet
pyglet.font.add_file('relogio digital/digital-7.ttf')

background = '#3d3d3d'
font_color = ['#fafcff', '#21c25c', '#eb463b', '#dedcdc', '#3080f0', '#32CD32']

root = Tk()
root.title('')
root.geometry('440x180')
root.resizable(False, False)
root.configure(bg=background)

def wacht():
    tempo = datetime.now()
    
    hora = tempo.strftime('%H:%M:%S')
    day_week = tempo.strftime('%A')
    day = tempo.day
    mes = tempo.strftime('%b')
    ano = tempo.strftime('%Y')
    
    color = random_color()
    
    lb_wacht.config(text=hora, fg=color)
    lb_wacht.after(800, wacht)
    l2.config(text=day_week +'\t'+ str(day) +'/'+ mes +'/'+ ano, fg=color)
    
def random_color():
    color = font_color.pop(0)
    font_color.append(color)
    return color

lb_wacht = Label(root, text='', font=('digital-7 100'), bg=background, fg=font_color[0])
lb_wacht.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(root, text='', font=('digital-7 20'), bg=background, fg=font_color[0])
l2.grid(row=1, column=0, sticky=NW, padx=5)
    
wacht()
root.mainloop()