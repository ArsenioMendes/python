num = int(input('Qual o valor para ser calculado a PA?: '))
raz = int(input('Qual a razão da PA?: '))
c = 0
print(f'calculando a PA de {num}')
print(num, end=' ')
while c < 9:
    num += raz
    print(f'>> {num}',end=' ')
    c += 1
print('Fim.')