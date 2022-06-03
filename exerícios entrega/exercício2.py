vetor = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 9, 10, 19, 23, 3, 4, 5, 6, 6, 9, 3]
contMais = 0
contMenos = 0
contIgual = 0

for x in range(len(vetor)):
    if vetor[x] > vetor[0]:
        contMais += 1
    elif vetor[x] < vetor[0]:
        contMenos += 1
    else:
        contIgual += 1
print(contMenos, contMais, contIgual)
