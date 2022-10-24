# Sequencia de Fibonacci

qtd_termos = int(input('Quantos termos da sequencia de Fibonacci quer que sejam representados?: '))
contador = 3
soma1 = 0
soma2 = 1
soma3 = 1

print(f'Iniciando sequencia de fibonacci com {qtd_termos} termos: ')
print(f'{soma1} → {soma2}', end='')
while contador <= qtd_termos: # Logica da sequencia de Fibonacci
    soma3 = soma1 + soma2
    print(f' → {soma3}',end='')
    soma1 = soma2
    soma2 = soma3
    contador += 1
print(' \nFim da sequencia.')