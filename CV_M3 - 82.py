lista = []
par = []
impar = []
valor = 0
opcao = 'S'

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor %2 == 0:
        par.append(valor)
        print(f'o valor {valor} foi inserido entre os pares.')
    else:
        impar.append(valor)
        print(f'o valor {valor} foi inserido entre os impares.')

    print('X'*50)
    opcao = str(input('DESEJA CONTINUAR ?'))
    if opcao in 'Nn':
        break
print('=-'*40)
print(f'Todos os valores = {lista}')
print(f'Valores impares = {impar}')
print(f'valores pares = {par}')