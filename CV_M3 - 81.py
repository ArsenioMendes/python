lista = []

totalvalores = 0
escolha = 's'

while True:
    lista.append(int(input('Digite um valor: ')))
    totalvalores += 1
    print('!'*30)
    escolha = str(input('DESEJA CONTINUAR [S/N]: '))
    if escolha in 'Nn':
        break

print('X'*100)
print(f'Foram digitados {totalvalores} números.')
print(f'A lista de valores em forma decrescente: {sorted(lista, reverse=True)}')

if 5 in lista:
    print('O valor 5 está contido na lista. ')
else:
    print('O valor 5 não consta na lista. ')