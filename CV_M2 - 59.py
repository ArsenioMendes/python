# Calculadora
def main():
    import time
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))
    opcao = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair\n>Selecione um opção: '))

    while opcao != 5:
        if opcao == 1:
            print(f'A soma de {num1} + {num2} = {num1 + num2}')
            opcao = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair\n>Selecione um opção: '))
        elif opcao == 2:
            print(f'A multiplicação entre {num1} * {num2} = {num1 * num2}')
            opcao = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair\n>Selecione um opção: '))
        elif opcao == 3:
            if num2 > num1:
                print(f'o valor {num2} é maior que o valor {num1}')
                opcao = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair\n>Selecione um opção: '))
            else:
                print(f'o valor {num1} é maior que o valor {num2}')
                opcao = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair\n>Selecione um opção: '))
        elif opcao == 4:
            print('---------Reinicando---------')
            main()
        else:
            print('Opção inválida, reiniciando código')
            time.sleep(2)
            print('---------Reinicando---------')
            main()
    exit()


main()
