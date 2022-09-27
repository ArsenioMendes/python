sexo = str(input('informe o seu sexo: [M/F] ')).upper()
while sexo not in 'MF':
    sexo = str(input('Dados incorretos, informe um sexo válido: [M/F]: ')).upper()
print(f'O sexo {sexo}, foi registrado! ')
