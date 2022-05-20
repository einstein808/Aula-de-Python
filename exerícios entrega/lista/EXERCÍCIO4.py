array = []
while True:
    temp = int(input("digites o valores  e valor 0 para sair"))
    if temp == 0:
        break
    else:
        array.append(temp)
contPar = 0
contN = 0
tamanho = len(array)


for x in range(len(array)):
    if array[x] % 2 == 0:
        contPar += 1
    else:
        contN += 1

porcentagem = contPar * 100 / tamanho
print(f"O total de Numeros Pares é {contPar}")
print(f"A quantidade de impares é {contN}")
print(f"{porcentagem}% são numeros pares.")
