'''
import sys
sys.stdin=open('input.txt','r')
'''
def selectmax(top, bottom):
    if (top==6 and bottom==5) or (top==5 and bottom==6):
        m=4
    elif top==6 or bottom==6:
        m=5
    else: m=6
    return m

def select(n, top,s):
    global maxn,N
    if n>N-1:
        if maxn<s:
            maxn=s
        return

    dice = arr[n]
    st=0
    while n<=N-1:
        if dice[st]==top:
            if st&1:
                nexttop=dice[st-1]
            else:
                nexttop=dice[st+1]
            select(n+1, nexttop,s+selectmax(top,nexttop))
            break
        st+=1


N = int(input())
tarr=[list(map(int, input().split())) for _ in range(N)]
arr=[[i[0],i[5],i[1],i[3],i[2],i[4]] for i in tarr]
maxn=0

for f in range(6):
    if f&1:
        select(1,arr[0][f],selectmax(arr[0][f],arr[0][f-1]))
    else:
        select(1,arr[0][f],selectmax(arr[0][f],arr[0][f+1]))

print(maxn)