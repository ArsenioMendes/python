#SOMA DE 6 VALORES PARES
n = 0
x = 0

for c in range(1, 7):
    n = int(input('digite um valor: '))
    if n % 2 == 0:
        x += n
print(f'O resultado da soma dos valores pares é: {x}')
