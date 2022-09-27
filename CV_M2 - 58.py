# Jogo da adivinhação
import random

tentativa = 0
n_comp = random.randint(1, 10)
n_esco = int(input('Digite o valor para a adivinhação: '))
print(f'foi selecionado o valor: {n_esco}')
while n_comp != n_esco:
    if n_comp > n_esco :
        n_esco = int(input('Mais... tente novamente: '))
        tentativa += 1
    else:
        n_esco = int(input('Menos... tente novamente: '))
        tentativa += 1
print(f'O valor {n_esco}, foi o que o PC escolheu, Parabéns!\nForam utilizadas {tentativa} tentativas.')