arrayCodigo = []
arrayValor = []
arrayAumento = []
while True:
    temp2 = int(input("digite o código e zero para sair"))

    if temp2 == 0:
        break
    else:
        temp = float(input("digite o valor"))
        arrayValor.append(temp)
        arrayCodigo.append(temp2)


for x in range(len(arrayValor)):
    aumento = arrayValor[x] * (1 + 20 / 100)
    arrayAumento.append(aumento)

for x in range(len(arrayCodigo)):
    print(f"o código {arrayCodigo[x]} ")
    print(f"seu novo valor é: {arrayAumento[x]}")
    print("************************")


aux = 0
contAn = 0
for x in range(len(arrayValor)):
    aux += arrayValor[x]
    contAn += 1
mediaAntigo = aux / contAn

print(f"a média do valores {mediaAntigo} ")

aux = 0
contNovo = 0
for x in range(len(arrayAumento)):
    aux += arrayAumento[x]
    contNovo += 1
mediaNovo = aux / contNovo
print(f"a média dos valores com aumento {mediaNovo} ")
