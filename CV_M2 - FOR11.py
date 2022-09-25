# média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
pessoa = 0
homem = 0
menor_20 = 0
idadet = 0
homem_mais_velho = 0
condicao = 0
for p in range(1, 5):
    pessoa += p
    sexo = int(input(f'qual o sexo da {p} pessoa?: (digite 1 para homem e 2 para mulher) '))

    if sexo == 1:  # calculo para homem.
        idadehomem = int(input(f'qual a idade do homem {p}?: '))
        nome = str(input(f'qual o nome da pessoa {p}?: '))
        idadet += idadehomem
        if condicao <= idadehomem:  # isto define a idade do homem mais velho
            homem_mais_velho = nome
            condicao = idadehomem
    else:
        idadem = int(input(f'qual a idade da mulher {p}?: '))
        idadet += idadem
        if idadem < 20:
            menor_20 += 1
idadet = idadet/4
print(f'------------------------------\nIdade média do Grupo: {idadet}\nHomem mais velho: {homem_mais_velho}\nQuantas '
      f'mulheres com menos de 20 anos: {menor_20}')
