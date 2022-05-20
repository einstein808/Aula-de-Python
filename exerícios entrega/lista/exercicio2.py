array = []

while True:
    temp = int(input("digite os valoes e 0 para sair"))
    if temp == 0:
        break
    else:
        array.append(temp)
contN = 0
cont = 0
soma = 0
contNum = 0
for x in range(len(array)):
    if array[x] < 0:
        contN += 1
    else:
        cont += 1
    soma += array[x]
    print(x)
contNum = contN + cont
mediaPositivo = cont * 100 / contNum
mediaNegativo = contN * 100 / contNum


print(f"a média é {soma / contNum}")
print(f"a quantidade de negativo {contN}")
print(f"a quantidade de positvos {cont}")
print(f"média de numero positivos é { mediaPositivo}% ")
print(f"a média dos Negativos é {mediaNegativo}%")
