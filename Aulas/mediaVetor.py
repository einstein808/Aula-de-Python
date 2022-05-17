def function(vetor):
    soma = 0
    cont = 0
    for x in vetor:
        soma += x
        cont += 1
    return (soma / cont)


print(function([5, 5, 5, 5, 5]))
