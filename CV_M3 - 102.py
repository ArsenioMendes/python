def fatorial(numero, show=True):
    numero = 1
    print(f'{num}!', end=' ')
    for c in range(num, 0, -1):
        numero *= c
        if show:
            print(f'x {c} ', end='')
    print()
    print(f'Resultado Fatorial = {numero}')


num = int(input('Digite um valor: '))
fatorial(num)
