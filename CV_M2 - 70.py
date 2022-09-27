total = mais1000 = mais_barato = preço = 0
mais_barato_nome = nome = continuar = 'a'
print('__________________________\n      LOJA BARATÃO\n__________________________')

while True:
    nome = str(input('Informe o produto: ')).upper().strip()
    preço = float(input('Informe o preço do produto: '))
    total += preço
    if preço >=1000:
        mais1000 += 1
    if mais_barato <= preço:
        mais_barato = preço
        mais_barato_nome = nome
    print('===================================')
    continuar = str(input('Deseja continuar?: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Preço total: {total:.2f} R$')
print(f'{mais1000} Produtos custam mais de 1000.00 R$')
print(f'O produto mais barato é {mais_barato_nome}, custando {mais_barato:.2f} R$.')
print('Fim do programa.')