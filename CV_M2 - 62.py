num = int(input('Qual primeiro termo da PA?: '))
raz = int(input('Qual a razão da PA?: '))
c = 0
qtd = 1
total = 0
print(num, end=' ')
while c < 9:
    num += raz
    print(f'>> {num}', end=' ')
    c += 1
print('PAUSA')
while qtd != 0:
    qtd = int(input('\nQuantos termos você quer que seja imprimido a mais (Pressione n para sair) ?: '))
    for ad in range(1, qtd+1):
        num += raz
        print(f'>> {num}', end=' ')
        total += qtd - 1
print(f'Progressão finalizada\n{total+10} de termos imprimidos')
