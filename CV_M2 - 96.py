def area(a, b):
    resultado = a * b
    print(f'A área do retângulo {a} X {b} é: {resultado} metros quadrados.')


def pontilhado(pont):
    print('--' * 30)
    print(pont)
    print('--' * 30)


pontilhado('MEDIDOR DE ÁREA')
largura = float(input('Digite o tamanho da largura: '))
altura = float(input('Digite o tamanho da altura: '))
area(altura, largura)
