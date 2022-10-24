from random import randint
from time import sleep

lista = []


def sorteio():
    print('SORTEANDO OS NÚMEROS... = ', end=' ')
    for num in range(0, 5):
        aleatorio = randint(0, 10)
        lista.append(aleatorio)
        sleep(0.3)
        print(aleatorio, end=' ')
    print('PRONTO!!')


def somapar():
    total = 0
    for num in lista:
        if num % 2 == 0:
            total += num
    print(f'A soma dos valores pares de {lista}, temos: {total}')


sorteio()
somapar()
