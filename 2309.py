#일곱 난쟁이
nlist=[]
for nan in range(9):
    nlist.append(int(input()))

def find(nlist):
    total=sum(nlist)
    for i in range(9):
        for j in range(i+1,9):
            if nlist[i]+nlist[j]==total-100:
                return nlist[i],nlist[j]

n1,n2=find(nlist)
nlist.remove(n1)
nlist.remove(n2)
nlist.sort()
for i in nlist:
    print(i)
