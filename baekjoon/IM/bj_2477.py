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

max=maxlist[0]*maxlist[1]

if abs(kmlist.index(maxlist[0]) - kmlist.index(maxlist[1]))==1:
    i = kmlist.index(maxlist[0])
    min = kmlist[i-2]*kmlist[i-3]
else:
    min=minlist[1]*minlist[2]

print((max-min)*melon)
    



        

