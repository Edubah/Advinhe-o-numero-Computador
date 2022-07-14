# Utilizar o módulo RANDOM. Uso de funções, laços while e condicionais e inputs
#Foco desse projeto é criar um jogo de advinhar um número

import random

def advinhar(x):

    numero_aleatorio = random.randint(1, x)

    advinhar = 0

    while advinhar != numero_aleatorio:

        advinhar = int(input(f'Número aleatório entre 1 e {x}: '))

        if advinhar < numero_aleatorio:
            print('Desculpe, adivinhe denovo, muito baixo desta vez!')

        elif advinhar > numero_aleatorio:
            print('Desculpe, adivinhe denovo, muito alto desta vez!')

    print(f'BOA!! Você advinhou o número {numero_aleatorio} corretamente!!!!! <3')

advinhar(10)