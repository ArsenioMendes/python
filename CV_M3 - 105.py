
def notas():
    nota = {'TOTAL': len(lista_nota), 'MAIOR': max(lista_nota), 'MEDIA': sum(lista_nota) / len(lista_nota)}
    print(nota)


continuar = 0
lista_nota = []
while True:
    lista_nota.append(input('Digite uma nota: '))
    continuar = int(input('999 encerra. '))
    if continuar == 999:
        break
notas()
