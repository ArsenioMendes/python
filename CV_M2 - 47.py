# IMPARES MULTIPLOS DE 3
soma = 0
cont = 0
for c in range(1, 500):
    if c % 3 == 0:
        if c % 2 != 0:
            cont += 1
            soma += c
print(f'soma de todos os impares multiplos de 3 é {soma}, {cont} valores registrados')