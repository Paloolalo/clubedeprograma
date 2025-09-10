nota1 = int (input('digite um numero:'))
nota2 = int (input('digite um numero:'))
nota3 = int (input('digite um numero:'))
nota4 = int (input('digite um numero:'))

resultado = (nota1 + nota2 + nota3 + nota4) / 4

print ('A media é:' + str (resultado))


if (resultado<=10) and (resultado>=6):
    print ('Aprovado')
elif (resultado<6) and (resultado>=5):
    print ('Recuperação')
elif (resultado < 5) and (resultado>=0):
    print ('Reprovado')
else : 
    print ('Valor Inválido')
