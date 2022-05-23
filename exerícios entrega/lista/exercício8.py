def perfeito(n):
    soma = 0
    for x in range(1, n):
        if n % x == 0:
            soma += x

    if soma == n:
        return True
    else:
        return False


arrayPerfeito = []
n = int(input('Exibir perfeitos até o número: '))
for val in range(1, n + 1):
    if(perfeito(val)):
        arrayPerfeito.append(val)
print(arrayPerfeito[0])
print(arrayPerfeito[1])
print(arrayPerfeito[2])
