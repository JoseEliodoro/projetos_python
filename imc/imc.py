from tkinter import *


#Modulos
from calc import calc

#classes
from widgets_entry import Widgets

class Imc():
    
    def __init__(self):
        self.root = Tk()
        self.window_config()
        self.create_frame()
        self.widgets = Widgets(self.root)
        self.widgets.widgets_frame_entry()
        self.widgets_frame_result()
        self.gender = 'm'
        
        self.root.mainloop()
        
    def window_config(self):
        self.root.title('Calculadora de IMC')
        self.root.geometry('271x371+600+200')
        self.root.resizable(False, False)
        
    
    def create_frame(self):
        
        self.frame_result = Frame(self.root, bg='#fff')
        self.frame_result.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)
        
    

    def widgets_frame_result(self):
        self.lb_result = Label(self.frame_result, bg='#fff', text='25,3 obesidada morbida', 
                               fg='#267AFA', font='League 12 bold')
        
        
        self.frame_border = Frame(self.frame_result, bg='#267AFA')
        self.frame_border.place(x=48, y=75, width=177, height=30)
        
        self.btn_calc = Button(self.frame_border, text='Calcular', bd=0, bg='#fff',
                               fg='#267AFA',  font='League 12 bold', command=self.calc)
        self.btn_calc.place(x=2, y=2, width=173, height=26)
        
    def calc(self):
        self.widgets.lb_error_height.place(x=-500, y=-500)
        self.widgets.lb_error_weight.place(x=-500, y=-500)
        verify = True
        try:
            weight = float(self.widgets.entry_weight.get())
            
        except ValueError:
            self.widgets.lb_error_weight.place(x=7, y=90)
            verify = False
        try:
            height = float(self.widgets.entry_height.get()) / 100
        except ValueError:
            self.widgets.lb_error_height.place(x=7, y=157)
            verify = False
        
        if verify:
            self.lb_result['text'] = calc(height, weight, self.gender)
            self.lb_result.pack()

    
Imc()