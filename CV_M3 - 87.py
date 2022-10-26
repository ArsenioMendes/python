num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = atribuicao = soma_terceira_coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        atribuicao = int(input(f'Insira o valor da da coordenada {l,c} = ')) # BLOCO DE ATRIBUIÇÃO DE VALOR ...
        num[l][c] = atribuicao
        if atribuicao % 2 == 0:
            somapar += atribuicao
print('-='*50)
for rl in range(0, 3):
    for rc in range(0, 3):
        print(f'[{num[rl][rc]:^5}]', end=' ') # BLOCO DE RESPOSTA ...
    print('')
print('-='*50)
print(f'A soma de todos os valores pares digitados = {somapar}.')
for s in range(0, 3): # BLOCO DE SOMA TERCEIRA COLUNA ...
    soma_terceira_coluna += num[s][2]
print(f'A soma dos valores da terceira coluna = {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha = {max(num[1])}.')