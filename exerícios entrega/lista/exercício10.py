valor = int(input("digite o valor "))
aux2 = 0


def fatorial(valor):
    aux = 1
    for x in range(1, valor + 1):
        aux *= x
    return aux


for x in range(1, valor + 1):
    aux2 += 1 / fatorial(x)
    print(aux2)

print(f"{aux2:.4f}")