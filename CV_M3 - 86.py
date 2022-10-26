num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        num[l][c] = int(input(f'Insira o valor da da coordenada {l,c} = '))
for rl in range(0, 3):
    for rc in range(0, 3):
        print(f'[{num[rl][rc]:^5}]', end=' ')
    print('')