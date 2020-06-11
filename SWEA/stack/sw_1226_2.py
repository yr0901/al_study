#미로1-교수님 재귀 버전

import sys
sys.stdin=open('input.txt','r')

def getsome(y,x):
    global found

    if not 0<=x<N or not 0<=y<N or maz[y][x]==1 or found==1: return
    if maz[y][x]==3:
        found=1
        return

    maz[y][x]=1

    getsome(y+1,x)
    getsome(y-1, x)
    getsome(y, x+1)
    getsome(y, x-1)


tcase = int(input())

for tc in range(1,tc+1):
    n=int(input())
    maz=[list(map(int, input().split())) for _ in range(16)]
    found=0
    y=x=1

    while found==0:
        getsome(y,x)

    print(f'#{tc+1} {found}')

