#창고 다각형
num=int(input())
#wlist=[]
hlist=[]
area=0
dic={}
for n in range(num): #입력
    w, h=map(int, input().split())
    hlist.append(h)
    dic.update({w:h})
    udic=sorted(dic.items())

hst= hlist.index(max(hlist)) 
i=0
while i<hst:
    temph=udic[i][1]
    tempw=udic[i][0]
    k=i+1
    while k<=hst:
        if udic[k][1]>temph:
            nextw=udic[k][0]
            break
        k+=1
    tw=nextw-tempw
    area+= tw*temph
    i=k

while i>hst and i<len(udic):
    i=-1
    tempw=udic[i][0]
    temph=udic[i][1]
    k=i-1
    while k>=hst:
        if udic[k][1]>temph:
            nextw=udic[k][0]
            break
        k-=1
    tw=tempw-nextw
    area+= tw*temph
    i=k

print(area+hlist[hst])