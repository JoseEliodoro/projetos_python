from pygame import mixer
from tkinter import *
from datetime import datetime
from time import sleep
from threading import Thread

janela = Tk()
janela.title('')
janela.geometry('350x150')
janela.resizable(False, False)


def tocar_alarme():
    mixer.music.load('../../../Music/Favela-Vive-2.mp3')
    mixer.music.play()
def alarme():
    while True:
        control = 1
        h_alarme = '09'
        m_alarme = '50'
        s_alarme = '50'
        p_alarme = 'pm'.upper()
        
        data = datetime.now()
        
        hora = data.strftime('%I')
        minuto = data.strftime('%M')
        segundo = data.strftime('%S')
        periodo = data.strftime('%p')
        
        if(control == 1):
            if(p_alarme == periodo):
                if(h_alarme == hora):
                    if(m_alarme == minuto):
                        if(s_alarme == segundo):
                            print('hora de fazer uma pausa')
                            tocar_alarme()
        sleep(1)
        
t1 = Thread(target=alarme)
t1.start()
mixer.init()

tocar_alarme()
janela.mainloop()