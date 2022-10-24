x = {'nome': str(input('Nome do jogador: '))}
totalpartidas = int(input(f'Quantas partidas {x["nome"]} jogou?: '))
gols = []

for c in range(1, totalpartidas + 1):
    gols.append(int(input(f'Quantos gols {x["nome"]} marcou no {c}º jogo?: ')))
x['gols'] = gols
x['total'] = sum(gols)
print('=-' * 40)
print(x)
print('=-' * 40)
for k, v in x.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 40)
print(f'O jogador {x["nome"]} jogou {totalpartidas} partidas.')
for pt in range(0, totalpartidas):
    print(f'  => Na partida {pt + 1}, fez {gols[pt]} gols.')
print(f'  => Totalizando {x["total"]} gols.')
