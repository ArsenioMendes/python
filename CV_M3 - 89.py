notas = []
aluno = []

continuar = escolha = 0

while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    aluno.append(float(input(f'Digite a primeira nota do aluno {aluno[0]}: ')))
    aluno.append(float(input(f'Digite a segunda nota do aluno {aluno[0]}: ')))
    notas.append(aluno[:])
    aluno.clear()
    continuar = str(input('Deseja inserir outro aluno? [S/N]: '))
    if continuar in 'Nn':
        break
print('-'*50)
print('N. --  NOME  --  MÉDIA.')
for c, v in enumerate(notas):
    print(c+1, end='')
    print(f'{notas[c][0]:>10}', end='')
    print(f'{(notas[c][1] + notas[c][2]) / 2:>10}')
print('-'*50)
while True:
    escolha = int(input('Exibir notas detalhadas? (Escolha um número referente a cada aluno, 999 interrompe.: '))
    if escolha == 999:
        print('Volte sempre.')
        break
    print(f'As notas de {notas[escolha-1][0]} foram: {notas[escolha-1][1]} e {notas[escolha-1][2]}')
