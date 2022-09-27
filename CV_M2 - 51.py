# NÚMERO PRIMO
num = int(input('digite o número para verificar se é primo: '))

for c in range(2,num-1):
    if num % c == 0:
        print(f'o valor {num}, não é primo')
        exit('fim')
print(f'o valor {num} é primo.')
