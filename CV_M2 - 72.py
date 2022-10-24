num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
       'trese', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

e = int(input('Escolha um número para se expresso em extenso: '))
while e > 20 or e < 0:
       e = int(input('número incorreto, digite novamente.'))

print(num[e])
