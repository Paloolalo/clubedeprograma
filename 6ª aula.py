def soma(num1, num2):
    resultado1 = num1 +  num2
    print (resultado1)
    
def subtracao(num1, num2):
    resultado2 = num1 - num2
    print (resultado2)  
    
def divisao(num1, num2):
    if num2 == 0: 
        print ('error')
    else: 
        resultado3 = num1 / num2
        print (resultado3)

def multiplicacao(num1, num2):
    resultado4 = num1 * num2
    print (resultado4)


while 1:
    operacao = input('informe qual operação você deseja fazer:')
    num1 = int (input('digite o primeiro número:'))
    num2 = int (input('digite o segundo número:'))

    
    if operacao == 'soma': soma (num1, num2)
    elif operacao == 'subtracao': subtracao (num1, num2)
    elif operacao == 'divisao': divisao (num1, num2)
    elif operacao == 'multiplicacao': multiplicacao (num1, num2)
    else: print: ('para de ser burro')
    cu = input('você deseja continuar?:')
    if cu == 'não' : 
        break
    
