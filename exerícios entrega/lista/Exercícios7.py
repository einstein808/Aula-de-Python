valores = []
for x in range(10):
    aux = int(input(f"digite o valor {x+1}: "))
    valores.append(aux)
cont = 0
contN = 0
print(valores)
for x in range(len(valores)):
    if valores[x] >= 10 and valores[x] <= 20:
        cont += 1
    else:
        contN += 1
print(f"Dos valores passados {cont} estão no  intervalor de 10 a 20")
print(f"Fora do intervalor são {contN}")