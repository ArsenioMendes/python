num = int(input('Digite um valor para calcular o fatorial: '))
mult = 1
print(f'Calculando o fatorial do valor {num}: ')
numb = num
print(f'{num}!', end=' ')
while num > 1:
    mult *= num
    num -= 1
    print(f'X {num}', end=' ')
print(f'= {mult} ')
