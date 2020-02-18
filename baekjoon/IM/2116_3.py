#주사위 쌓기
import sys
sys.stdin=open('input.txt', 'r')

def match(bottom, top):
    global N
    if len(tlist[-1])==2:
        for x in range(N-1):
            summ+=max(dlist[x])
        if summ>supermax:
            supermax=summ

    for d in range(dnum-1):
        for i in range(6):
            if dlist[d][i]==top:
                if i&1:
                    newbottom=dlist[d][i]
                    newtop=tlist[d][0]
                    dlist[d].remove(newtop)
                    dlist[d].remove(newbottom)
                    match(newbottom, newtop)
                else:
                    newbottom=tlist[d][0]
                    newtop=tlist[d][1]
                    dlist[d].remove(newtop)
                    dlist[d].remove(newbottom)
                    match(newbottom, newtop)


dnum=int(input())
dlist=[list(map(int, input().split())) for _ in range(dnum)]
supermax=0

for d in range(dnum):
    mlist=tlist[d]
    for i in range(2):
        if i&1:
            bottom=mlist[0]
            top=mlist[1]
            match(bottom, top)
        else:
            bottom=mlist[1]
            top=mlist[1]
            
