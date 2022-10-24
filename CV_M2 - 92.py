ctps = {}
ctps['NOME'] = str(input('NOME: '))
ctps['NASCIMENTO'] = int(input('ANO DE NASCIMENTO: '))
ctps['IDADE'] = 2022 - ctps['NASCIMENTO']
ctps['CTPS'] = int(input('CARTEIRA DE TRABALHO (0 - NÃO CONSTA): '))
if ctps['CTPS'] != 0:
    ctps['CONTRATAÇÃO'] = int(input('ANO DE CONTRATAÇÃO: '))
    ctps['SALÁRIO'] = int(input('SALARIO: R$ '))
print('=-'*40)
ctps['IDADE DE APOSENTADORIA'] = ctps['CONTRATAÇÃO'] - ctps['NASCIMENTO'] + 35
for k, v in ctps.items():
    print(f' - {k} tem o valor: {v}')