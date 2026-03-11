import random

opções = ['tesoura', 'papel', 'pedra']

while 1:
    computador = opções[random.randint(0,2)]

    pessoa = input("Jokenpô: ")


    print(computador)

    if (pessoa == 'tesoura' and computador == 'papel'): print ('Droga... Você ganhou...')
    elif (pessoa == 'tesoura' and computador == 'pedra'): print ('Chupa porra! Você perdeu!')
    elif (pessoa == 'tesoura' and computador == 'tesoura'): print ('Putz... Empate..')
    elif (pessoa == 'papel' and computador == 'papel'): print ('Putz... Empate..')
    elif (pessoa == 'papel' and computador == 'tesoura'): print ('Chupa porra! Você perdeu!')
    elif (pessoa == 'papel' and computador == 'pedra'): print ('Droga... Você ganhou...')
    elif (pessoa == 'pedra' and computador == 'pedra'): print ('Putz... Empate..')
    elif (pessoa == 'pedra' and computador == 'tesoura'): print ('Chupa porra! Você perdeu!')
    elif (pessoa == 'pedra' and computador == 'papel'): print ('Droga... Você ganhou...')

    sair = input('sair?: ')
    if sair == 'sim' : break   
