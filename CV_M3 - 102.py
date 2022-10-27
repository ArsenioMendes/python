def fatorial(numero, show=True):
    """
    -> Calculador de fatorial.
    :param numero: Valor a ser usado no fatorial.
    :param show: Exibe o valores anteriores que vão compor o fatorial.
    :return: retorna o valor final do fatorial.
    """
    print(f'{numero}! =', end=' ')
    total = 1
    for f in range(numero, 0, -1):
        total *= f
        if show:
            print(f'{f}', end=' ')
            if f > 1:
                print(f'x', end=' ')
            else:
                print('=', end=' ')
    return total


num = int(input('Digite um valor para o fatorial: '))
print(fatorial(num, show=True))
