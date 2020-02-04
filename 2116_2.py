dnum=int(input())
dlist=[list(map(int, input().split())) for _ in range(dnum)]
mlist=[[[k[0],k[5]], [k[1], k[3]], [k[2], k[4]]] for k in dlist]
print(mlist)

anwlist=[]
def stack(temp, t):
    for i in range(3):
        if t in temp[i]:
            
            print(temp)
            tmp = temp[0]+temp[1]
            max_n = max(tmp)
            break
    return max_n

for n in range(6):
    t=n+1
    alist=[]
    for d in range(dnum):
        temp=mlist[d]
        print(f'temp={temp}')
        print(stack(temp,t))
        alist.append(stack(temp, t))
        for tp in temp:
            if t in tp:
                tp.remove(t)
                t=tp[0]
                break
    anwlist.append(sum(alist))

print(max(anwlist))