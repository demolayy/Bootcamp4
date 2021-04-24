import random
import os
import time

# numero aleatorio
numeroSelecionado = random.randrange(101)


def dica():  # dica
    if numero > numeroSelecionado:
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

numero = None
numeroSelecionado = random.randrange(101)
while True:
    try:
        numero = int(input('Chute um numero:'))
        if type(numero) == int:
            if numero == numeroSelecionado:
                print("Muito bem você acertou!")
                print("Você quer jogar novamente?")
                retry = input('S/N?')
                if retry in ("N", "NAO"):
                    print("Obrigado por jogar!")
                    exit()
                elif retry in ("S", "SIM"):
                    cls()
                    numeroSelecionado = random.randrange(101)
                    continue
            elif numero != numeroSelecionado:
                cls()
                dica()
                continue
    except ValueError:
        print("Digite um numero Inteiro!!")
        time.sleep(0.8)
        cls()
