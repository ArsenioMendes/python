num = media = soma = maior = termos = menor = 0
continuar = 'S'


print('Executando programa...')
while continuar == 'S':

    num = int(input('Digite um valor: '))
    termos += 1
    soma += num
    if termos == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    continuar = str(input(f'Já registrados {termos}, deseja continuar o programa?: [S/N] ')).upper()
    print(f'Soma de todos os valores: {soma}')
print('~'*30)
print(f'~Programa finalizado\n~A média entre os valores escolhidos foi {soma/termos}\n~O maior valor foi {maior}\n~O '
      f'menor valor foi {menor}')
