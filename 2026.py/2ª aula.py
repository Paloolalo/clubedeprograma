#5<= ca => 100
while 1:
    idade1= int(input('digite a idade de celeste: '))
    if idade1>= 5 and idade1 <= 100:
        break
    else:
        print ('idade inválida')
while 2:
    idade2= int(input('digite a idade de cibele: '))
    if idade2>= 5 and idade2 <= 100:
        break
    else:
        print ('idade inválida')
while 3:
    idade3= int(input('digite a idade de camila: '))
    if idade3>= 5 and idade3 <= 100:
        break
    else:
        print ('idade inválida')

if idade3 > idade1 > idade2:
    print ('celeste')
elif idade2> idade1 > idade3:
    print ('celeste')
if idade3 > idade2 > idade1:
    print ('cibele')
elif idade1> idade2 >idade3:
    print ('cibele')
if idade1> idade3 >idade2:
    print ('camila')
elif idade2 > idade3 >idade1:
    print ('camila')
else: print ('idade inválida')
