#참외밭
melon=int(input())
tlist=[]
drlist=[]
kmlist=[]
maxlist=[]
minlist=[]

for n in range(6):
    dr, km = map(int, input().split())
    drlist.append(dr)
    kmlist.append(km)

for i in range(6):
    if drlist.count(drlist[i])==1:
        maxlist.append(kmlist[i])
    else:
        minlist.append(kmlist[i])
max=min=1
for k in range(2):
    max*=maxlist[k]

for t in range(4):
    if t==1 or t==2:
        min*=minlist[t]

print((max-min)*melon)
    



        

