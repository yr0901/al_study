#미로
import sys
sys.stdin=open('input.txt','r')

def issafe(nexty, nextx):
    if nexty>=0 and nexty<=N-1 and nextx>=0 and nextx<=N-1 and visited[nexty][nextx]==0 and arr[nexty][nextx]!=1:
        return True

def getsome(startx, starty):
    global anw
    if arr[starty][startx]==3:
        anw=1
        return
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    visited[starty][startx]=1
    
    for i in range(4):
        nextx=startx+dx[i]
        nexty=starty+dy[i]
        if issafe(nexty, nextx):
            getsome(nextx, nexty)
    return      

tcase = int(input())
for tc in range(tcase):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    anw=0
    visited=[[0 for _ in range(N)] for _ in range(N)]
    #2찾기
    for x in range(N):
        for y in range(N):
            if arr[y][x]==2:
                startx=x
                starty=y
                break
    #미로 찾기
    getsome(startx, starty)
    print('#{} {}'.format(tc+1, anw))

