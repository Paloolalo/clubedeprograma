import random

opções = ["cara", "coroa"]

sorteio = random.randint(0, 1)
jogada = input("Escolhe cara ou coroa!: ").lower()

if jogada == opções[sorteio]:
    print("Você ganhou!")
    input("precionene enter para sair")

else:
    print("Você perdeu!")
    input("precionene enter para sair")