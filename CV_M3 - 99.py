from random import randint
from time import sleep


def maior(*x):
    print(f'BLOCO {total+1} ↓')
    for num in range(0, randint(1, 10)):
        lista.append(randint(1, 10))
    print('=-' * 30)
    print('ANALISANDO VALORES ALEATÓRIOS...')
    for val in lista:
        sleep(0.3)
        print(val, end=' ')
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {max(lista)}.')
    lista.clear()
    print('=-' * 30)
    print()


lista = []
total = 0

for times in range(1, randint(2, 7)):
    maior(lista)
    total += 1
print('X'*40)
print(f'FORAM PRINTADOS {total} BLOCOS DE CÓDIGOS.')