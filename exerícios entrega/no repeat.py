p1= [1,2,3,8,9]
p2 = [1,2,3,11,12]
p3=[]
p1ToP2 = p1[:]

p1ToP2.extend(p2)
print(p1ToP2)
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
