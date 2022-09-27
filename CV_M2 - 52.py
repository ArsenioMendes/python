#PALINDROMOS

frase = str(input('qual a frase a ser analisada?: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso +=junto[letra]
if inverso == junto :
    print(f'temos um palindromo: {inverso, junto} ')
else:print(f'a frase {frase}, não é um palindromo')

