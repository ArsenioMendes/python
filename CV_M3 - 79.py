lista = []

lista.append(int(input('Digite um valor: ')))
while True:
    print('-='*50)
    escolha = input('QUER CONTINUAR?: [S/N]')
    if escolha in 'Nn':
        break
    val = int(input('Digite um valor: '))
    if val not in lista:
        lista.append(val)
        print('Valor adicionado com sucesso !')
    else:
        print('Este valor já consta na lista, não será adicionado.')

print('*'*100)
print(f'Código finalizado, os números escolhidos em ordem crescente foram = {sorted(lista)}')