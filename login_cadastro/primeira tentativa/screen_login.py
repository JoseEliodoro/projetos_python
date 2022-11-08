from distutils.cmd import Command
from tkinter import *

#Minhas clases
from settings import Settings
from placeholder import PlaceHolder as Ph
from new_button import New_button

class Screen():
    def __init__(self, root):
        self.root = root
        self.ai_settings = Settings()
        self.setting_screen()
        #self.create_widgets()
        self.frame()
        self.gender = False #False para masculino/ True para feminino
        
    
    def setting_screen(self): #Configuração da tela
     
        self.root.geometry(self.ai_settings.dimension_login)        
        self.root.title('Tela de login')
        self.root.resizable(False, False)
        self.img_login = PhotoImage(file='img/screen_login.png')
        
        #Label de imagem de login
        self.lb_login = Label(self.root, image=self.img_login)
        self.lb_login.pack()
        
        
    
    def create_widgets(self):
            
        #Botão de login
        self.btn_login = New_button(self.lb_login, color1='#ccc', bd=0, text='LOGIN', cursor='hand2', bg='#fff', fg='#407aff', font='Condensed 15 bold')
        self.btn_login.config()
        self.btn_login.place(x=20, y=434, width=370, height=50)
        
        #entrada de login
        self.entry_username = Ph(self.lb_login, 'LOGIN', '#f5f5f5', show=None, bd=0, font='Arial 20 bold', bg='#407aff', fg='#fff')
        self.entry_username.entry.place(x=19, y=147, width=374)
        
        #Entrada de senha
        self.entry_password = Ph(self.lb_login, 'SENHA', '#f5f5f5', show='*', bd=0, font='Arial 20 bold', bg='#407aff', fg='#fff')
        self.entry_password.entry.place(x=19, y=265, width=373)
        
        #Label para cadastrar
        self.lb_text_cad = Label(self.lb_login, text='Faça o cadastro', underline=True, bg='#407aff', fg='#fff', font='Condensed 11 bold')
        self.lb_text_cad.place(relx=0.37, rely=0.74)
        
        
        self.lb_text_cad.bind('<Button>', self.frame)
       
        
    def frame(self, *args):
        
        self.lb_login.place(x=-1000, y=-1000)
        
        self.root.geometry(self.ai_settings.dimension_cad) 
        
        self.img_cad = PhotoImage(file='img/screen_cadastro.png')
        #Label de imagem de Cadastro
        self.lb_cad = Label(self.root, image=self.img_cad)
        self.lb_cad.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        #Entrada de cadastro username
        self.entry_username_cad = Ph(self.lb_cad, 'NOME DE USUÁRIO', '#f5f5f5', show=None, bd=0, font='Arial 20 bold', bg='#407aff', fg='#fff')
        self.entry_username_cad.entry.place(x=19, y=147, width=374)
           
        
        self.lb_invalid_username = Label(self.lb_cad, bg='#407aff', text='Nome de usuário inválido',font='Arial 10 bold', fg='#ff0000')
        self.lb_invalid_username.place(x=19, y=187)
        
        #Entrada de cadastro email
        self.entry_email_cad = Ph(self.lb_cad, 'E-MAIL', '#f5f5f5', show=None, bd=0, font='Arial 20 bold', bg='#407aff', fg='#fff')
        self.entry_email_cad.entry.place(x=19, y=265, width=374)
        
        self.lb_invalid_username = Label(self.lb_cad, bg='#407aff', text='E-mail inválido',font='Arial 10 bold', fg='#ff0000')
        self.lb_invalid_username.place(x=19, y=305)   
           
        #Entrada de cadastro name
        self.entry_name_cad = Ph(self.lb_cad, 'NOME', '#f5f5f5', show=None, bd=0, font='Arial 20 bold', bg='#407aff', fg='#fff')
        self.entry_name_cad.entry.place(x=19, y=383, width=374)
        
        self.lb_invalid_username = Label(self.lb_cad, bg='#407aff', text='Nome inválido',font='Arial 10 bold', fg='#ff0000')
        self.lb_invalid_username.place(x=19, y=423)
              
        #Entrada de cadastro password
        self.entry_password_cad = Ph(self.lb_cad, 'SENHA', '#f5f5f5', show='*', bd=0, font='Arial 20 bold', bg='#407aff', fg='#fff')
        self.entry_password_cad.entry.place(x=413, y=147, width=374)
        
        self.lb_invalid_username = Label(self.lb_cad, bg='#407aff', text='Senha inválida',font='Arial 10 bold', fg='#ff0000')
        self.lb_invalid_username.place(x=413, y=187)
           
        #Entrada de cadastro confirm_password
        self.entry_confirm_password_cad =  Ph(self.lb_cad, 'CONFIRMAR SENHA', '#f5f5f5', show='*', bd=0, font='Arial 20 bold', bg='#407aff', fg='#fff')
        self.entry_confirm_password_cad.entry.place(x=413, y=265, width=374) 
        
        self.lb_invalid_username = Label(self.lb_cad, bg='#407aff', text='Senhas diferentes',font='Arial 10 bold', fg='#ff0000')
        self.lb_invalid_username.place(x=413, y=305)
         
        #Botão de masculino
        self.btn_man = New_button(self.root, color1='#5098ff', bg='#407aff', bd=0, text='MASCULINO', cursor='hand2', fg='#fff', font='Condensed 15 bold' , command=self.trace_gender)
        self.btn_man.config()
        self.btn_man.place(x=432, y=385, width=170, height=50)
           
        #Botão de feminino
        self.btn_woman = New_button(self.root, color1='#ccc', bg='#fff', bd=0, text='FEMININO', cursor='hand2', fg='#407aff', font='Condensed 15 bold', command=self.trace_gender)
        self.btn_woman.config()
        self.btn_woman.place(x=603, y=385, width=170, height=50)

        #Botão de cadastro
        self.btn_cad = New_button(self.root, color1='#ccc', bd=0, text='CADASTRO', cursor='hand2', bg='#fff', fg='#407aff', font='Condensed 15 bold', command=self.cad)
        self.btn_cad.config()
        self.btn_cad.place(x=232, y=537, width=370, height=50) 
        
        
    def trace_gender(self):
        if(self.gender):
            self.btn_woman.defi('#ccc', '#fff')
            self.btn_woman['fg'] = '#407aff'
            
            self.btn_man.defi('#5098ff', '#407aff')
            self.btn_man['fg'] = '#fff'
            
            self.gender = False
        else:
            self.btn_man.defi('#ccc', '#fff')
            self.btn_man['fg'] = '#407aff'
            
            self.btn_woman.defi('#5098ff', '#407aff')
            self.btn_woman['fg'] = '#fff'
            
            self.gender = True
            
            
    def cad(self):
        username = self.entry_username_cad.get()
        email = self.entry_email_cad.get()
        password = self.entry_password_cad.get()
        confir_password = self.entry_confirm_password_cad.get()
        name = self.entry_name_cad.get()
        
    
root = Tk()       
a = Screen(root)
    
root.mainloop()