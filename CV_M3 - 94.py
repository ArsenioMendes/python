lista = []
pessoa = {}
sexo = continuar = numpessoa = somaidade = 0

while True:
    pessoa['NOME'] = str(input('NOME: '))  # BLOCO NOME
    numpessoa += 1

    sexo = str(input('SEXO [M/F]: ')).upper()  # BLOCO SEXO
    while sexo not in 'MmFf':
        sexo = str(input('ERRADO, DIGITE M OU F: ')).upper()
    pessoa['SEXO'] = sexo

    pessoa['IDADE'] = int(input('IDADE: '))  # BLOCO IDADE
    somaidade += pessoa['IDADE']
    lista.append(pessoa.copy())
    pessoa.clear()

    continuar = str(input('CONTINUAR [S/N]?: '))  # BLOCO CONINUE
    while continuar not in 'SsNn':
        continuar = str(input('ERRADO, CONTINUAR [S/N]?: '))
    if continuar in 'nN':
        break

print(f'{lista}')
print('=-' * 40)
print(f'A) Ao todo temos = {numpessoa} pessoas cadastradas.')
media = somaidade/numpessoa
print(f'B) A média de idade é = {media:5.2f} anos.')
print(f'C) As mulheres na lista foram: ', end='')
for p in lista:
    if p['SEXO'] == 'F':
        print(f'{p["NOME"]} ', end='')
print()
print('D) Pessoas com idade acima da média: ')
for p in lista:
    if p['IDADE'] > media:
        print(f'NOME= {p["NOME"]}, SEXO= {p["SEXO"]}, IDADE= {p["IDADE"]} ')
print(f' <=ENCERRADO=> ')
