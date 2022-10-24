
n1 = int(input('Digite o Primeiro valor: '))
n2 = int(input('Digite o Segundo valor: '))
n3 = int(input('Digite o Terceiro valor: '))
n4 = int(input('Digite o Quarto valor: '))
noves = 0

num = (n1, n2, n3, n4)

for x in num:
    if x == 9:
        noves += 1
print(f'A quantidade de números 9 foi: {noves}')
if 3 in num:
    print(f'Posição do valor 3 : {num.index(3)}')
else:
    print('O valor 3 não consta nessa tupla')

for x in num :
    if x % 2 == 0:
        print(f'O valor {x}, é par.')
