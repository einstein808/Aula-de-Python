lista = [1, 2, 3, 3, 4, 4, 5, 6, 8, 9, 1]
armanament0 = {}
for x in lista:
    if x in armanament0:
    	armanament0[x] = [i for i, item in enumerate(lista) if item == x]
    else:
    	armanament0[x] = lista.index(x)

print(armanament0)
