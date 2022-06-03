vet = [1, 2, 4, 7, 4, 2, 8, 9, 0, 6, 5, 4, 3]
print(len(vet))
print("")
print(vet[3])
print(vet[7])
# print(vet[13])
print(vet[9])
print("******")
vet[1] = vet[3] * vet[1]
print(vet[1])
vet[10] = vet[3]**2 + vet[0]
print(vet[10])

vet[6] = vet[vet[5]]
print(vet[6])
vet[11] = vet[7] / vet[12]
print(vet[11])

vet[2] = vet[3]**3 + vet[0]
print(vet[2])

vet[6] = vet[10] + vet[1] - vet[8]
print(vet[6])

print(vet)
print(vet[1], vet[10], vet[6], vet[11], vet[2], vet[6])
