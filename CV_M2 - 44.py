peso = float(input('qual o peso ?'))
altura = float(input('qual a altura?'))

imc = peso / (altura **2)

if imc < 18.5:
    print(f'abaixo do peso com o IMC{imc:.2f}')
elif imc < 25:
    print(f'peso ideal com IMC {imc:.2f}')
elif imc < 30:
    print(f'sobrepeso com IMC {imc:.2f}')
elif imc < 40 :
    print(f'obesidade com IMC {imc:.2f}')
else :
    print(f'obesidade morbida com IMC {imc:.2f}')

