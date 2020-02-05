#창고 다각형
num=int(input())
wlist=[]
hlist=[]
area=0

for n in range(num): #입력
    w, h = map(int, input().split())
    wlist.append(w)
    hlist.append(h)
    
hst= hlist.index(max(hlist)) 
i=0
while i<hst:
    temph=hlist[i]
    tempw=wlist[i]
    k=i+1
    while k<=hst:
        if hlist[k]>temph:
            nextw=wlist[k]
            break
        k+=1
    tw=nextw-tempw
    area+= tw*temph
    i=k

while i>hst and i<len(wlist):
    nextw=hlist.index(max(hlist[i+1:]))
    tw=wlist[nextw]-wlist[hst]
    area+=tw*hlist[nextw]
    i=nextw

print(area+hlist[hst])