games = []
i=0
vitória = 0
while i < 6:
    games.append (input(f"digite o resultado do {i+1}º jogo:"))
    i+=1
vitória = 0
for game in games:
    if game == 'V':
        vitória+=1
if vitória == 5 or vitória == 6:
    print ('1')
elif vitória == 3 or vitória == 4:
    print ('2')
elif vitória == 1 or vitória == 2:
    print ('3')
else:

    print ("-1")