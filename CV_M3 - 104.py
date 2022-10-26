def leiaint(x):
    while True:
        if x.isnumeric():
            print(f'Você digitou o número {x}')
            break
        else:
            x = input(f'ERRO O {x} INFORMADO NÃO É UM NÚMERO, DIGITE UM NÚMERO INTEIRO: ')


num = input('Digite um numero: ')
leiaint(num)
