def triangulo():
    base = int(input('digite o valor da base:'))
    altura = int(input('digite o valor da altura:'))
    return (base*altura)/2
    
def quadrado():
    lado = int(input('digite o valor do lado'))
    return lado**2
   
    
def retangulo():
    base = int(input('digite o valor da base:'))
    altura = int(input('digite o valor da altura:'))
    return base*altura
 
def trapezio():

    base_maior = int(input('digite o valor da base maior:'))
    base_menor = int(input('digite o valor da base menor:'))
    altura = int(input('digite o valor da altura:'))
    return ((base_maior+base_menor)*altura)/2  

def main():
    print('1 - Triângulo')
    print('2 - Quadrado')
    print('3 - Retângulo')
    print('4 - Trapézio')
    opcao = int(input('Digite a opção desejada:'))
    
    if opcao == 1:
        print(triangulo())
    elif opcao == 2:
        print(quadrado())
    elif opcao == 3:
        print(retangulo())
    elif opcao == 4:
        print(trapezio())
    else:
        print('Opção inválida')

main()