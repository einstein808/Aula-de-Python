p1= []
p2 = []
p3=[]
while True:
    n = int(input(" digites os valores da lista 1 e 0 para sair"))
    if n==0:
        break
    p1.append(n)
while True:
    b = int(input("digite os valorers l2 0 para sair"))
    if b==0:
        break
    p2.append(b)

p1ToP2 = p1[:]

p1ToP2.extend(p2)
x = 0
while x < len(p1ToP2):
    y=0
    while y <len(p3):
        if p1ToP2[x]==p1ToP2[y]:
            break
        y+=1
    if y==len(p3):
        p3.append(p1ToP2[x])
    x +=1
print(p3)
