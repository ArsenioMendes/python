lista = []
par = []
impar = []
esc = 'S'

while True:
    lista.append(int(input('Digite um valor: ')))
    print('--'*30)
    esc = str(input('Deseja continuar?[S/N]: '))
    if esc in 'Nn':
        break
for i, v in enumerate(lista):
    if v %2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('XX'*60)
print(f'Os valores são: {lista}')
print(f'Os valores pares são: {par}')
print(f'Os valores impares são: {impar}')
