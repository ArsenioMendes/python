time = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians', 'Internacional', 'Cruzeiro',
        'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Fluminense', 'Coritiba', 'Bahia', 'Goiás', 'Guarani', 'Sport',
        'Portuguesa', 'Atlético Paranaense', 'Vitória')

num = time.index('Bahia')
print('~-'*10, 'sistema de classificação dos clubes de futebol brasileiros'.upper(), '~'*10)
print(f'5 Primeiros colocados:\n{time[0:5]}\n', '-='*70)
print(f'4 Ultimos colocados:\n{time[-4:]}\n', '-='*70)
print(f'Times em ordem alfabética:\n{sorted(time)}\n', '-='*70)
print(f'Posição do Bahia: {num}')
