tc=int(input())

def group(tmp):
    slist=[]
    tp=[]
    for i in tmp: # 두개씩 묶기
        tp.append(i)
        if len(tp)==2:
            slist.append(tp)
            tp=[]
    return slist

for tcase in range(tc):
    i=0
    clist=[]
    num=int(input())
    tmp = list(map(int, input().split()))
    nlist=[]
    slist=group(tmp)

    for i in range(len(tmp)):
        clist.append(tmp.count(tmp[i]))

    gclist = group(clist)
    anlist=[]

    for i  in range(num):
        if gclist[i]==[1,2]:
            anlist.append(slist[i])
    i=0
    while i<num: 
        if gclist[i] ==[2,2] and anlist[-1][1]==slist[i][0]:
            anlist.append(slist[i])
            i=0
            continue
        i+=1


    for i in range(num):
        if gclist[i]==[2,1]:
            anlist.append(slist[i])

    tl=[]
    for t in anlist:
        for d in range(2):
            tl.append(t[d])

    print(f'#{tcase+1}', end=' ')
    print(*tl)            
        