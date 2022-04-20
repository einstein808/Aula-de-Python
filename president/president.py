voto=[]
while True:
    n = int(input("digite um voto , 0 sai"))
    if n==0:
        break
    voto.append(n)
cad1=0
cand2=0
cand3=0
cand4=0
votob=0
voton=0
for x in voto:
    if x ==1:
        cad1+=1
    if x ==2:
        cand2+=1
    if x ==3:
        cand3+=1
    if x ==4:
        cand4+=1
    if x ==6:
        votob +=1
    if x !=1 and x!=2 and x!=3 and x!=4 and x!=6:
        voton+=1


total= cad1+cand2+cand3+cand4+votob+voton
print(f'total de votos = {total}')
print(f'canditato 1 ={cad1}'
      f'  candidato 2 ={cand2}'
      f'  candidato 3 ={cand3}'
      f'  candidato 4 ={cand4}'
      f'  voto nulo ={voton}'
      f'  voto branco ={votob}')