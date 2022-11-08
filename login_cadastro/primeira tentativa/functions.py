from tkinter import *

def hover_button(button, color1, color2):
    button.bind('<Enter>', func=lambda e: button.config(
            background= color1
    ))
        
    button.bind('<Leave>', func=lambda e: button.config(
        background=color2
    ))
    