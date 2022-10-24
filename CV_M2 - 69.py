idade = homem = mulher = mais18 = 0
sexo = restart = 'm'
print('============ Registro de pessoas ============')
while True:
    print('===============================')
    idade = int(input('Qual a idade da pessoa?: '))
    sexo = str(input('Qual o sexo da pessoa?: ')).strip().upper()[0]
    print('===============================')
    if idade >= 18:
        mais18 += 1
    if sexo == 'H':
        homem += 1
    if sexo == 'M':
        if idade < 20:
            mulher += 1
    print('===============================')
    restart = str(input('Deseja questionar novamente?: ')).strip().upper()[0]
    if restart == 'N':
        break
print('===============================')
print(f'{mais18} pessoas tem mais de 18 anos.')
print(f'{homem} São homens.')
print(f'{mulher} mulheres tem menos de 20 anos.')
