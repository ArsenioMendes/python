import random

escolha = int(input("Digite um número referente a sua escolha\n Pedra: 1\n Tesoura: 2\n papel: 3 \nDigite a sua opção: "))

escolha_pc = random.randint(1, 3)

print(f'o pc escolheu {escolha_pc}')

if escolha == escolha_pc:
    print('empate')
elif escolha == 1 and escolha_pc == 3:
    print('vitoria do pc')
elif escolha == 2 and escolha_pc == 1:
    print('vitoria do pc')
elif escolha == 3 and escolha_pc == 2:
    print('Vitoria do pc')
else:
    print('Sua vitoria')
