valores = []
escolha = 0

while True:
    valores.append(int(input('Digite um valor')))
    escolha = int(input('digite 666 para sair'))
    if escolha == 666:
        break

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v} !')
print('cheguei ao fim da lista')