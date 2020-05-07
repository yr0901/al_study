import sys
sys.stdin=open('input.txt','r')

def devide(tlist, start, end):
    global win, anw
    if end-start==1:
        if tlist[start]==tlist[end]:
            return start
        if win[tlist[start]]==tlist[end]:
            return start
        else:
            return end
    if end==start:
        return end

    pivot=(start+end)//2
    lwin = devide(tlist, start, pivot)
    rwin = devide(tlist, pivot+1, end)
    if tlist[lwin]==tlist[rwin]:
        anw=lwin
    elif win[tlist[lwin]] == tlist[rwin]:
        anw=lwin
    else:
        anw=rwin
    return anw

tcase=int(input())
for tc in range(tcase):
    N=int(input())
    tlist=list(map(int, input().split()))
    win={2:1, 3:2, 1:3}

    start=0
    end=N-1
    devide(tlist,start,end)
    print('#{} {}'.format(tc+1,anw+1))
'''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''
T = int(input())
N = None
cards = None

def verse(idx1,idx2):
    if cards[idx1]==cards[idx2]:
        return idx1
    if cards[idx1]==1:
        if cards[idx2]==2:
            return idx2
    elif cards[idx1]==2:
        if cards[idx2]==3:
            return idx2
    elif cards[idx1]==3:
        if cards[idx2]==1:
            return idx2
    return idx1

def getResult(start,end):
    if start==end:
        return start
    elif start+1==end:
        return verse(start,end)
    else:
        mid = (start+end)//2
        first = getResult(start,mid)
        second = getResult(mid+1,end)
        return verse(first,second)

for tc in range(1,T+1):
    N = int(input())
    cards = list(map(int,input().split()))
    print("#{0} {1}".format(tc,getResult(0,N-1)+1))