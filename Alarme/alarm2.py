from tkinter.ttk import *
from tkinter import *
from customtkinter import *
#from time import sleep

#Meus modulos
from hour_controler import UpDown
from function import *
import pyglet
from datetime import datetime
from despetador import Toque

#Tela

class Alarm():
    def __init__(self): 
        self.root = CTk()
        
        img = PhotoImage(file='despertador1.png')
        active = Button(self.root, image=img, bg='#000', bd=0, command=self.set_alarm)
        active.place(relx=.75 ,rely=0.73)
        
        self.list = list()

        self.day = int(datetime.now().strftime('%w'))

        self.screen_config()
        self.widgets_set_alarme()
        
        now(self.c_hora, self.c_hora2,
            self.c_minuto1, self.c_minuto2, self.btns_week)
        self.root.mainloop()
     

    
    def screen_config(self): #Configuração de screen
        
        self.root.title('Alarme 1.2')
        self.root.geometry('300x168+200+400')
        #self.root.resizable(False, False)
        self.root.config(background='#000')
        
    
    def widgets_set_alarme(self):
        pyglet.font.add_file('../relogio digital/digital-7.ttf')
        
        self.c_hora = Label(self.root, text="8", font='digital-7 70', width=1, justify='right', 
                  fg='#0DC400', bg='#000')
        self.c_hora2 = Label(self.root, text="8", font='digital-7 70', width=1, justify='right',
                        fg='#0DC400', bg='#000')


        
        digit_hora =  UpDown(0, 24, datetime.now().strftime('%H'))
        self.btn_up_hora = CTkButton(self.root, text='', cursor='hand2',
                           command=lambda: up(digit_hora, self.c_hora, self.c_hora2))
        self.btn_down_hora = CTkButton(self.root, text='', cursor='hand2',
                             command=lambda: down(digit_hora, self.c_hora, self.c_hora2))
        
        
        self.c_minuto1 = Label(self.root, text="8", font='digital-7 70', 
                               width=1, justify='right', fg='#0DC400', bg='#000')
        self.c_minuto2 = Label(self.root, text="8", font='digital-7 70', 
                               width=1, justify='right', fg='#0DC400', bg='#000')
        
        

        digit_minuto = UpDown(0, 60, datetime.now().strftime('%M'))
        self.btn_up_minuto = CTkButton(self.root, text='', cursor='hand2',
                           command=lambda: up(digit_minuto, self.c_minuto1, self.c_minuto2))
        self.btn_down_minuto = CTkButton(self.root, text='', cursor='hand2',
                             command=lambda: down(digit_minuto, self.c_minuto1, self.c_minuto2))
        
        
        self.ponto = Label(self.root, text=":", font='digital-7 80', justify='right', 
                  fg='#0DC400', bg='#000')
        
        self.day_week()
            
        
        
        
        self.widgets_position()
        
        
        
    def day_week(self):
        radiobutton = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        
        def events(btn):
            btn.bind('<Enter>', lambda args: hover_up(btn, args))
            btn.bind('<Leave>', lambda args: hover_down(btn, args))
            btn.bind('<Button>', lambda args: color_selected(btn, args))
            
        def hover_up(btn, *args):
            btn['bg'] = '#222'
            
        def hover_down(btn, *args):
            btn['bg'] = '#000'
            
        def color_selected(btn, *args):
            for button in self.btns_week:
                button['fg'] = '#0D6400'
            btn['fg'] = '#0DC400'
            value = 0
            if('dom' == btn['text'].lower()):
                value = 1
            elif('seg' == btn['text'].lower()):
                value = 2
            elif('ter' == btn['text'].lower()):
                value = 3
            elif('qua' == btn['text'].lower()):
                value = 4
            elif('qui' == btn['text'].lower()):
                value = 5
            elif('sex' == btn['text'].lower()):
                value = 6
            elif('sab' == btn['text'].lower()):
                value = 7
            self.day = value
            
        x = 0.01
        self.btns_week = list()
        for day in radiobutton:
            btn = Button(self.root, text=day.upper(),
                         bd=0, bg='#000',
                         fg='#0D6400',font='digital-7 12', width=3)
            events(btn)
            btn.place(relx=x, rely=.73)
            
            self.btns_week.append(btn)
            
            x += 0.105

    def widgets_position(self):
        self.c_hora.place(relx=.01, rely=.23, relheight=.4)
        self.c_hora2.place(relx=.15, rely=.23, relheight=.4)

        self.c_minuto1.place(relx=.45, rely=.23, relheight=.4)
        self.c_minuto2.place(relx=.59, rely=.23, relheight=.4)
        
        self.ponto.place(relx=.34, rely=.23, relheight=.4)
        
                
        self.btn_up_hora.place(relx=.034, rely=.16, relheight=.03, relwidth=.26)
        self.btn_down_hora.place(relx=.034, rely=.66, relheight=.03, relwidth=.26)
        
                
        self.btn_up_minuto.place(relx=.46, rely=.16, relheight=.03, relwidth=.26)
        self.btn_down_minuto.place(relx=.46, rely=.66, relheight=.03, relwidth=.26)
        
        
    """ def test(self):
        self.list[0].stop() """
        
    def set_alarm(self):
        hour =  self.c_hora['text'] + self.c_hora2['text']
        minute = self.c_minuto1['text'] + self.c_minuto2['text']
        self.list.append(Toque('alarm.mp3', hour, minute, self.day))
        

""" def up(end, digit1, digit2):
    hora = str(digit1['text']) + str(digit2['text'])
    if(int(hora) == 0):
        if(int(end[1]) == 9):
            digit2['text'] = 0
            digit1['text'] = int(end[0]) +1
        else:
            digit2['text'] = int(end[1]) + 1
            digit1['text'] = int(end[0])
    else: 
        h2 = int(digit2['text']) - 1
        if(h2 >= 0):
            digit2['text'] = h2
        else:
            digit2['text'] = 9
            digit1['text'] = int(digit1['text']) + 1

def down(max, digit1, digit2):
    hora = str(digit1['text']) + str(digit2['text'])
    if(int(hora) == 0):
        if(int(max[1]) == 0):
            digit2['text'] = 9
            digit1['text'] = int(max[0]) -1
        else:
            digit2['text'] = int(max[1]) - 1
            digit1['text'] = int(max[0])
    else: 
        h2 = int(digit2['text']) - 1
        if(h2 >= 0):
            digit2['text'] = h2
        else:
            digit2['text'] = 9
            digit1['text'] = int(digit1['text']) - 1
        """


""" import threading
class at():
    def __init__(self, sair):
        self.va = False
        self.c_hora = sair
    
    def test(self):
        while self.va:
            print('a')
            down()
            sleep(.2)
    
    def tet(self, *a):
        self.va = True
        self.t1= threading.Thread(target=self.test)
        self.t1.start()
    
    def ta(self, *a):
        self.va = False
        self.t1.join()

tt = at(c_hora) 
c_hora.bind('<Button>', tt.tet)
c_hora.bind('<ButtonRelease>', tt.ta) """   


Alarm()