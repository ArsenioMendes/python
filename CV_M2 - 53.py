#PESSOAS COM MAIORIDADE
maioridade = 0
menoridade = 0

for c in range(1, 8):
    pessoa = int(input(f"qual a idade da pessoa número: {c} ? "))
    if pessoa >= 21:
        maioridade += 1
    else: menoridade += 1
print(f'[{maioridade}] pessoas estão na maioridade, [{menoridade}] pessoas estão na menoridade.')