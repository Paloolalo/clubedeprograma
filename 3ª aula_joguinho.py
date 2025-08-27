import random

numero = random.randint(1,100)


palpite = 0 
tentativa = 0 


while 1:
    tentativa += 1
    
    print ('tentativa' + str(tentativa))
    palpite = int(input('Digite o seu palpite!:'))
    if palpite <= 0 or palpite > 100:
        print ('número inválido')
        continue
    
    
    if palpite == numero:
        print ('Você Acertou!!')
        break
    elif palpite > numero:
        print ('O palpite é maior que o número')
    elif palpite < numero:
        print ('O palpite é menor que o número')
