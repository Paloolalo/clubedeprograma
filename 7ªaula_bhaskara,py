def delta (a,b,c):
    resultado = (b**2) - (4 * a * c)
    return resultado
    
def raizpositiva(a, b, delta):
    resultado = (-b + delta**0.5)/ (2*a)
    return resultado
    
def raiznegativa(a, b, delta):
    resultado = (-b + delta**0.5)/ (2*a)
    return resultado
    
val_a = int(input('a:'))
val_b = int(input('b:'))
val_c = int(input('c:'))

delta = delta (val_a, val_b, val_c)

x1 = raizpositiva(val_a, val_b, delta)
x2 = raiznegativa(val_a, val_b, delta)

if delta < 0:
    print('raiz negativa')
    
else:
    
    print (f'O resultado foi {x1} e {x2}')
