def calc(height, weight, gender):
    imc = weight / (height ** 2)
    txt = '%.2f'%(imc)
    if(gender == 'm'):
        if(imc < 20.7):
            txt += ' Abaixo do peso.'
        elif(imc >= 20.7 and imc < 26.4):
            txt += ' Peso ideal.'
        elif(imc >= 26.4 and imc < 27.8):
            txt += ' Pouco acima do peso.'
        elif(imc >= 27.9 and imc < 31.1):
            txt += ' Acima do peso.'
        elif(imc >= 31.1 and imc < 35.5):
            txt += ' Obesidade.'
        elif(imc > 38.5):
            txt += ' Obesidade mórbida.'
            
    if(gender == 'f'):   
        if(imc < 19.1):
            txt += ' Abaixo do peso.'
        elif(imc >= 19.1 and imc < 25.8):
            txt += ' Peso ideal.'
        elif(imc >= 25.8 and imc < 27.3):
            txt += ' Pouco acima do peso.'
        elif(imc >= 27.3 and imc < 32.3):
            txt += ' Acima do peso.'
        elif(imc >= 32.3 and imc < 35.2):
            txt += ' Obesidade.'
        elif(imc > 35.2):
            txt += ' Obesidade mórbida.'
    return txt