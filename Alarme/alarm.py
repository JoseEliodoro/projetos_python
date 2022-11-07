from time import sleep
from tkinter.ttk import *
from tkinter import *
from pygame import mixer

from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread


cor0 = '#f0f3f5'
cor1 = '#feffff'
cor2 = '#d6872d'
cor3 = '#fc766d'
cor4 = '#403d3d'
cor5 = '#4a88e8'


janela = Tk()
janela.title('')
janela.geometry('350x150')
janela.configure(background=cor1)
janela.resizable(False, False)

frame_logo = Frame(janela, width=400, height=10, bg=cor2)
frame_logo.grid(row=0, column=0, pady=1, padx=0)

frame_corpo = Frame(janela, width=400, height=140, bg=cor1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0)
img = PhotoImage(file='icon-sun.png')

l_linha = Label(frame_corpo, image=img, width=100, height=100, bg=cor1, anchor=NW,
                font='Ivy 16 bold', compound=LEFT, padx=10, fg=cor3)
l_linha.place(x=10, y=10)

l_nome = Label(frame_corpo, text='Alarme', height=1, bg=cor1, anchor=NE,
                font='Ivy 10', fg=cor4)
l_nome.place(x=105, y=10)


l_hora = Label(frame_corpo, text='hora', height=1, bg=cor1, anchor=NW,
                font='Arial 7', fg=cor4)
l_hora.place(x=130, y=40)
value = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11')
c_hora = Combobox(frame_corpo, width=2, font='Ivy 15', values=value)
c_hora.current(0)
c_hora.place(x=130,y=58)

value = list(value)
for x in range(12, 60):
    value.append(x)

l_minuto = Label(frame_corpo, text='minuto', height=1, bg=cor1, anchor=NW,
                font='Arial 7', fg=cor4)
l_minuto.place(x=180, y=40)
c_minuto = Combobox(frame_corpo, width=2, font='Ivy 15', values=value)
c_minuto.current(0)
c_minuto.place(x=180,y=58)

l_segundo = Label(frame_corpo, text='Segundo', height=1, bg=cor1, anchor=NW,
                font='Arial 7', fg=cor4)
l_segundo.place(x=230, y=40)
c_segundo = Combobox(frame_corpo, width=2, font='Ivy 15', values=value)
c_segundo.current(0)
c_segundo.place(x=230,y=58)

l_dia = Label(frame_corpo, text='Periodo', height=1, bg=cor1, anchor=NW,
                font='Arial 7', fg=cor4)
l_dia.place(x=280, y=40)
c_dia = Combobox(frame_corpo, width=3, font='Ivy 15', values=('PM', 'AM'))
c_dia.current(0)
c_dia.place(x=280,y=58)


def ativar_alarme():
    #print(selecionado.get())
    if selecionado.get() == 0:
        print('Ativar:', selecionado.get())
    else:
        t1 = Thread(target=alarme)
        t1.start()
    #print(c_hora.get(), c_minuto.get(), c_segundo.get(), c_dia.get())
    
    
def desativar_alarme():
    print('Alarme desativado: ', selecionado.get())
    mixer.music.stop()
    
    
selecionado = IntVar()
radio = Radiobutton(frame_corpo, text='Ativar', value=1, variable=selecionado, 
                    font='Arial 8', bg=cor1, fg=cor4, command=ativar_alarme)
radio.place(x=125, y=95)



def tocar_alarme():
    mixer.music.load('../../../Music/Favela-Vive-2.mp3')
    mixer.music.play()
    
    selecionado.set(0)
    
    radio = Radiobutton(frame_corpo, text='desativar', variable=selecionado, 
                    font='Arial 8', bg=cor1, fg=cor4, command=desativar_alarme)
    radio.place(x=187, y=95)



def alarme():
    while True:
        control = selecionado.get()
        
        h_alarme = c_hora.get()
        m_alarme = c_minuto.get()
        s_alarme = c_segundo.get()
        p_alarme = c_dia.get().upper()
        
        data = datetime.now()
        
        hora = data.strftime('%I')
        minuto = data.strftime('%M')
        segundo = data.strftime('%S')
        periodo = data.strftime('%p')
        print(f"{hora}/{minuto}/{segundo}\t{periodo}\t\t{h_alarme}/{m_alarme}/{s_alarme}\t{p_alarme}")
        if(control == 1):
            if(p_alarme == periodo):
                if(h_alarme == hora):
                    if(m_alarme == minuto):
                        if(s_alarme == segundo):
                            print('hora de fazer uma pausa')
                            tocar_alarme()
                            ativar_alarme()
        sleep(1)
        


mixer.init()

    
janela.mainloop()