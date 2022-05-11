
n = int(input("digite quantos numeros fatoriais "))
dados = []
cont = 0
while cont < n:
    aux = int(input(f"digite valor {cont + 1}: "))
    dados.append(aux)
    cont += 1
print(dados)
