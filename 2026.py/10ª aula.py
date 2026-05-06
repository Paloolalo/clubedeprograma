import random as rd 
num = rd.randint(1,100)

print ("acerta o numero ai seu viado!")

while 1:
    
    chute = int(input("chuta qualquer um:"))

    if chute > num:
        print ("tá achando que é o numero de transas da sua mãe? chuta mais baixo")
        continue 
    
    if chute < num:
        print ("não é tão baixo assim né seu merda, é maior")
        continue
    
    if chute == num:
        print ("acertou seu merda! fez algo útil da sua vida!")
        break
