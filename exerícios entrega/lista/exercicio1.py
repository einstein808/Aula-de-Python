
n = int(input("digite quantos numeros fatoriais "))
dados = []
cont = 0
final = 1
while cont < n:
    aux = int(input(f"digite valor {cont + 1}: "))
    cont += 1
    for x in range(1, aux + 1):
        final *= x
    print(final)
    final = 1
    x = 1
