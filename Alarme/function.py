from datetime import datetime

def up(obj, digit1, digit2):
    obj.incremente()
    if(len(str(obj.hora)) == 1):
        hora = '0'+ str(obj.hora)
    else:
        hora = str(obj.hora)
    digit1['text'] = hora[0]
    digit2['text'] = hora[1]
    
def down(obj, digit1, digit2):
    obj.decremente()
    if(len(str(obj.hora)) == 1):
        hora = '0'+ str(obj.hora)
    else:
        hora = str(obj.hora)
    digit1['text'] = hora[0]
    digit2['text'] = hora[1]
 
def now(hour1, hour2, minute1, minute2, btns_week):
    agora = datetime.now()
    hora = agora.strftime('%H')
    minuto = agora.strftime('%M')
    day = int(agora.strftime('%w'))
    hour1['text'] = str(hora[0])
    hour2['text'] = str(hora[1])

    minute1['text'] = str(minuto[0])
    minute2['text'] = str(minuto[1])
    
    btn = btns_week[day]
    
    btn['fg'] ='#0DC400'
    
    
    
    