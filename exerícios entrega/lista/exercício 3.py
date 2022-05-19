array = []2
while True:
    temp = int(input("digites o valores  e valor ngativo para sair"))
    if temp < 0:
        break
    else:
        array.append(temp)
intervalo1 = 0
intevalo2 = 0
intervalo3 = 0
intervalo4 = 0
for x in range(len(array)):
    if array[x]<=25:
        intervalo1+=1
    elif array[x]<=50:
        intevalo2+=1
    elif array[x]<=75:
        intervalo3+=1
    elif array[x]<=100:
        intervalo4+=1

print(intervalo1,intevalo2,intervalo3,intervalo4)
