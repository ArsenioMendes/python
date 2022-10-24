from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i}, até {f}, no passo {p} em {p} ...')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ')
            sleep(0.3)
            cont += p
        print('FIM !')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ')
            sleep(0.3)
            cont -= p
        print('FIM !')


print('A) ', end=' ')
contador(1, 10, 1)
print('B) ', end=' ')
contador(10, 0, 2)
print('CONTAGEM PERSONALIZADA: ')
print('C) ', end=' ')
inicio = int(input('Inicio = '))
fim = int(input('fim = '))
passo = int(input('passo = '))
if passo < 0:
    passo = passo * (-1)
if passo == 0:
    passo += 1
contador(inicio, fim, passo)
