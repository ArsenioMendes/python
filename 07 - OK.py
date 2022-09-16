nomes=['pessoa1', 'pessoa2','pessoa3', 'pessoa4', 'pessoa5', 'pessoa6', 'pessoa7', 'pessoa8', 'pessoa9', 'pessoa10']

id=0
qtd=0

for nom in nomes:
    print(nom)
    id=int(input("qual a idade da pessoa acima ?"))
    if id>=18:
        qtd=qtd+1
print("quantidade de pessoas com 18 anos ou mais= ", qtd, "pessoas")
