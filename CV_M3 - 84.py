lista = []
pessoa = []
continuar = 'S'
qtd = 0

while True:
    pessoa.append(int(input('Digite o PESO dessa pessoa: ')))
    pessoa.append(str(input('Digite o NOME da pessoa: ')))
    lista.append(pessoa[:])
    continuar = str(input('Deseja continuar?:[S/N] '))
    pessoa.clear()
    qtd += 1
    print('-'*50)
    if continuar in 'Nn':
        break

lista = sorted(lista)
lengh = len(lista)
half = lengh//2

print(f'Foram cadastradas: {qtd} pessoas.')
print(f'Pessoas mais pesadas: {lista[half:]}')
print(f'Pessoas mais leves: {lista[:half]}')

