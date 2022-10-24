import random
mega = []
valor = cont = 0

print('¨'*50)
print(' '*10, 'GERADOR DE JOGOS DA MEGA')
print('_'*50)

jogos = int(input('Quantos jogos você quer que eu sorteie?: '))
print(f'++++++++++ SORTEANDO {jogos} JOGOS ++++++++++')

for j in range(0, jogos):
    while True:
        valor = random.randint(0, 60)
        if valor not in mega:
            mega.append(valor)
            cont += 1
        if cont >= 6:
            break
    print(f'Jogo número {j+1}: {sorted(mega)}')
    mega.clear()
    cont = 0