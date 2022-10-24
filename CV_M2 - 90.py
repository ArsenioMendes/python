dados = {}

dados['nome'] = str(input('Digite o nome do aluno: '))
dados['media'] = int(input('Digite a média do aluno: '))
print('=-'*50)
if dados['media'] >= 7:
    dados['situação'] = 'APROVADO'
elif 5 <= dados['media'] < 7:
    dados['situação'] = 'RECUPERAÇÃO'
else : dados['situação'] = 'REPROVADO'
for k, v in dados.items():
    print(f' - O {k} é igual a {v} ')
