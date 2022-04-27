def contarImpar(n1,n2):
    limpar=[]
    if n1<n2:
        for x in range(n1,n2+1):
            if x%2 !=0:
                limpar.append(x)
    if n2<n1:
        for y in range(n2,n1+1):
            if y%2!=0:
                limpar.append(y)
    print(limpar)
contarImpar(1,10)