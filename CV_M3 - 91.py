from random import randint
from time import sleep
from operator import itemgetter
numeral = 1
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = dict()
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('=-='*30)
print(f'{"== RANKING DOS JOGADORES ==":^70} ')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'                      Em {numeral}º, o {v[0]} com {v[1]}.')
    numeral += 1