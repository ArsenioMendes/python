l1 = int(input('qual o valor do lado um ?'))
l2 = int(input('qual o valor do lado dois ?'))
l3 = int(input('qual o valor do lado tres ?'))

if l1 == l2 == l3:
    print("triangulo equilatero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("triangulo isosceles")
else: print("triangulo escaleno")
