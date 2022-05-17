def function(vetor):
    l3 = []
    for x in vetor:
        if x >= 0:
            l3.append(x)
        else:
            l3.append(0)
    return l3


print(function([1, 2, 3, -1, 0, 10]))
