vetor = [1, 2, 3, 4, 31, 32, 33, 34]
print(vetor)
contM30 = 0
soma30 = 0
somaTudo = 0
for x in range(len(vetor)):
    if vetor[x] > 30:
        contM30 += 1
        soma30 += vetor[x]
    somaTudo += vetor[x]
print(contM30, soma30, somaTudo)