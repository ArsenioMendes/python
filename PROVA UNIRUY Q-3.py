matriz = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
linhas = len(matriz)
coluna = len(matriz[0])

transposta = []

for j in range(coluna):
    linha = []
    for i in range(linhas):
        linha.append(matriz[i][j])
    transposta.append(linha)
print(transposta)
