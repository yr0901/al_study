dnum=int(input())
dlist=[list(map(int, input().split())) for _ in range(dnum)]
anw=0

anwlist=[]

def mklist(k, tmp):
    if k==0:
        tmp=tmp[1:5]
    elif k==1:
        tmp=[tmp[0]]+[tmp[2]]+tmp[4:]
    elif k==2:
        tmp=tmp[:2]+[tmp[3]]+[tmp[5]]
    return max(tmp)

for i in range(3):
    temp=[]
    for num in range(dnum):
        tmp=dlist[num]
        if num==0:
            temp.append(mklist(i,tmp))
            t=tmp[i]
        else:
            temp.append(mklist(tmp.index(t),tmp))
            t=dlist[num+1][t]
            
    anwlist.append(sum(temp))
print(max(anwlist))