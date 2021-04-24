import random
import os
import time

# numero aleatorio
numberSelected = random.randrange(101)

# dica


def dica():
    if number > numberSelected:
        print("Tente um numero menor")
    else:
        print("Tente um numero maior")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    text = input("Aperte enter para começar...")
    if text == "":
        cls()
        print(
            "Um número de 0 a 100 foi gerado\nagora você precisa adivinhar o numero gerado")
        break
    else:
        print("Você ainda não apertou o Enter")
        cls()

number = None

while True:
    try:
        print(numberSelected)
        number = int(input('Chute um numero:'))
        if type(number) == int:
            if number == numberSelected:
                print("Muito bem você acertou!")
                print("Você quer jogar novamente?")
                retry = input('S/N?')
                if retry in ("N", "NAO"):
                    print("Obrigado por jogar!")
                    exit()
                elif retry in ("S", "SIM"):
                    print("vamos jogar novamente")
                    cls()
                    numberSelected = random.randrange(101)
                    continue
            elif number != numberSelected:
                cls()
                dica()
                continue
    except ValueError:
        print("Digite um numero Inteiro!!")
        time.sleep(0.8)
        cls()
