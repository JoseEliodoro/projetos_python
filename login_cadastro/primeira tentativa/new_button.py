from tkinter import Button
import os
class New_button(Button):
    def __init__(self, root, color1='#fff', **argfs):
        super().__init__(root, argfs)
        self.color1 = color1
        self.color2 = self['bg']
        self.function_button()
    
    def function_button(self):
        self.bind('<Enter>', self.defcolor1)
        
        self.bind('<Leave>', self.defcolor2)
        
    def defcolor1(self, *args):
        self['bg'] = self.color1
    
    def defcolor2(self, *args):
        self['bg'] = self.color2
    
    def defi(self, color1, color2):
        self.color1 = color1
        self.color2 = color2
        self['bg'] = color2