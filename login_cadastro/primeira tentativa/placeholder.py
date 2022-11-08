from tkinter import *

class PlaceHolder(Entry):
    def __init__(self, root, placeholder='', color = '#989898', show=None, **args):
        self.entry = Entry(root, args)
        self.placeholder = placeholder
        self.default_color = self.entry['fg']
        self.color = color
        self.show = show
        
        self.placeholder_out()
        self.setting()
        
    def setting(self):
        self.entry.bind('<FocusIn>', self.placeholder_in)
        
        self.entry.bind('<FocusOut>', self.placeholder_out)
        
    def get(self):
        if(self.entry.get() == self.placeholder):
            return None
        return self.entry.get()
        
    def placeholder_in(self, *args):
        if(self.entry['fg'] == self.color and self.entry.get() == self.placeholder):
            self.entry.delete('0', 'end')
            self.entry['fg'] = self.default_color
            self.entry['show'] = self.show
            
    def placeholder_out(self,  *args):
        if(self.entry.get() == ''):
            self.entry['show'] = ''
            self.entry.insert(0, self.placeholder)
            self.entry['fg'] = self.color 
            