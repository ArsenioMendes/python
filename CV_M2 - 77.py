palavras = ('ESTUDAR', 'FOCO', 'DISCIPLINA', 'TREINO', 'METAMORFOSE', 'DINHEIRO', 'SIGMA')

for p in palavras:
    print(f'\n Na palavra {p} temos: ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(f'{letra}', end='')
    print(' vogais')