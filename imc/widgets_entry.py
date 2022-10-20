from tkinter import *
from functools import partial

class Widgets():
    def __init__(self, root):
        self.root = root
        self.frame_entry = Frame(self.root, bg='#fff')
        self.frame_entry.place(relx=0, rely=0, relwidth=1, relheight=0.7)
    
    def widgets_frame_entry(self):
        color = '#267AFA'
        #Labels de informação
        self.lb_title = Label(self.frame_entry, text='Calculadora de IMC'.upper(),
                              bg='#fff', font='League 16 bold', fg=color)
        self.lb_title.pack()
        
        self.lb_weight = Label(self.frame_entry, text='Peso'.upper(),
                              bg='#fff', font='League 12 bold', fg=color)
        self.lb_weight.place(x=7, y=63)
        
        self.lb_height = Label(self.frame_entry, text='Altura'.upper(),
                              bg='#fff', font='League 12 bold', fg=color)
        self.lb_height.place(x=7, y=130)
        
        self.lb_gender = Label(self.frame_entry, text='Gênero'.upper(),
                              bg='#fff', font='League 12 bold', fg=color)
        self.lb_gender.place(x=7, y=205)
        
        #Entrada do peso
        self.entry_weight = Entry(self.frame_entry, width=16,font='league 12 ', 
                                  bd=0, highlightbackgr=color, highlightthickness=1)
        self.entry_weight.place(x=109, y=63)
        
        #Label de erro no peso
        self.lb_error_weight = Label(self.frame_entry, text='Insira um valor válido para a peso'.upper(),
                              bg='#fff', font='League 6 bold', fg='#ff0000')
        
        #Entrada da altura
        self.entry_height = Entry(self.frame_entry, width=16,font='league 12',
                                  bd=0, highlightbackground=color, highlightthickness=1)
        self.entry_height.place(x=109, y=130)
        
        #Label de erro na altura
        self.lb_error_height = Label(self.frame_entry, text='Insira um valor válido para a altura'.upper(),
                              bg='#fff', font='League 6 bold', fg='#ff0000')
        
        #Botão para escolher gênero masculino
        self.btn_gender_man = Button(self.frame_entry, text='Homem', fg='#fff', font='league 12',
                                  bd=0, bg=color, command= self.change_gender) 
        self.btn_gender_man.place(x=109, y=205, width=70)
        self.btn_gender_man['command'] = partial(self.change_gender, self.btn_gender_man['text'])
        
        #Botão para escolher gênero feminino
        self.btn_gender_woman = Button(self.frame_entry, text='Mulher', fg=color, font='league 12',
                                  bd=0, command= self.change_gender)
        self.btn_gender_woman.place(x=186, y=205, width=70)    
        self.btn_gender_woman['command'] = partial(self.change_gender, self.btn_gender_woman['text'])
        
    def change_gender(self, verify):
        if(verify.lower() == 'homem'):
            self.btn_gender_woman['fg'] = '#267AFA'
            self.btn_gender_woman['bg']= 'SystemButtonFace'
            self.btn_gender_man['bg'] = '#267AFA'
            self.btn_gender_man['fg']= '#fff'
            self.gender = 'm'
        else:
            self.btn_gender_man['fg'] = '#267AFA'
            self.btn_gender_man['bg']= 'SystemButtonFace'
            self.btn_gender_woman['bg'] = '#267AFA'
            self.btn_gender_woman['fg']= '#fff'
            self.gender = 'f'