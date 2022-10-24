import math

v1 = [5, 4, 3]
v2 = [10, 9, 1]

totalv1 = totalv2 = 0

for c in v1:
    totalv1 += c

for x in v2:
    totalv2 += x

norma1 = math.sqrt(totalv1)
norma2 = math.sqrt(totalv2)
if norma1 > norma2:
    print('O vetor 1 tem a maior norma.')
else:
    print('O vetor 2 tem a maior norma.')
