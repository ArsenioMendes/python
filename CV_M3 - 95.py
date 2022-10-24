team = []
jogador = {}
gol = []
partidas = continuar = escolha = 0

while True:
    jogador['NOME'] = str(input('Digite o nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {jogador["NOME"]} jogou?: '))
    for g in range(0, partidas):
        gol.append(int(input(f'quantos gols foram marcados na partida {g + 1} ?: ')))
    jogador['GOLS'] = gol.copy()
    team.append(jogador.copy())
    gol.clear()
    jogador.clear()
    continuar = str(input('Deseja inserir outro jogador ? [S/N]: '))
    if continuar in 'Nn':
        break
print('='*100)
print(f'Codigo-↓     Nome-↓     Gols-↓     Total-↓')
print('='*100)
for c in range(0, len(team)):
    print(f'{c} ----- {team[c]["NOME"]} ----- {team[c]["GOLS"]} ----- {sum(team[c]["GOLS"])}')
print('='*100)

escolha = int(input('Mostrar dados de qual jogador?: (999 para parar) '))

while True:
    for x in range(0, len(team[escolha]['GOLS'])):
        print(f'No jogo {x+1} foram marcados {team[escolha]["GOLS"][x]}')
    escolha = int(input('Mostrar dados de qual jogador?: (999 para parar) '))
    if escolha == 999:
        break

#RODOU CARALHO !!!!!!!!!!!!!!!!!!!!!!!!!!!