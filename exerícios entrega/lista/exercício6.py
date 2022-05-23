numeroN = int(input("digite o numero"))
soma = 1
cont = 0
for x in range(1, numeroN + 1):
    soma += x / numeroN
    print(x)
    cont += 1

print(f"foi gerado total de {cont} termos e soma igual a: {soma}")
