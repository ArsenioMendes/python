lista = []
segundomenor = segundomaior = 0

for val in range(1, 6):
    lista.append(int(input(f'Digite o valor na posição {val}: ')))
print('=-' *50)

menorvalor = min(lista) # calculo do menor valor

print(f'O menor valor foi: {menorvalor} -- ', end=' ')

for i, v in enumerate(lista):
    if v == menorvalor:
        print(f'Na posição: {i+1}', end=' ')

maiorvalor = max(lista) # calculo do maior valor
print(f'\nO maior valor foi: {maiorvalor} -- ', end=' ')
for i, v in enumerate(lista):
    if v == maiorvalor:
        print(f'Na posição: {i+1}', end=' ')
