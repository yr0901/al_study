nlen=int(input())
nlist=list(map(int, input().split()))
temp=[nlist[i]-nlist[i+1] for i in range(nlen-1)]
ptemp=[0]*len(temp)
mtemp=[0]*len(temp)

#증가 =1세기
for k in range(len(temp)):
    if temp[k]<=0:
        ptemp[k]=1
#감소 =1세기
for k in range(len(temp)):
    if temp[k]>=0:
        mtemp[k]=1

pcount=mcount=maxn=0

#증가
for i in range(len(temp)):
    if ptemp[i]==1:
        pcount+=1
    else:
        if pcount!=0 and pcount!=1:
            if maxn<pcount:
                maxn=pcount
        pcount=0

#감소
for i in range(len(temp)):
    if mtemp[i]==1:
        mcount+=1
        if maxn<mcount:
            maxn=mcount
    else:
        if mcount!=0 and mcount!=1:
            if maxn<mcount:
                maxn=mcount
        mcount=0
print(maxn+1)