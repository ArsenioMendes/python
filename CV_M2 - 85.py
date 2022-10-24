lista = [[], []]
val = 0
for c in range(1, 8):
    val = int(input(f'Digite o {c}º valor: '))
    if val % 2 == 0:
        lista[0].append(val)
    else:
        lista[1].append(val)
print(f'Valores pares: {sorted(lista[0])}')
print(f'Valores impares: {sorted(lista[1])}')
