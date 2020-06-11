#행렬찾기
import sys
sys.stdin = open('input.txt','r')

def DFS(tempy , tempx):
    global maxx, maxy

    visited[tempy][tempx]=True
    if maxx<tempx:
        maxx=tempx
    if maxy<tempy:maxy=tempy

    for d in range(4):
        nexty = tempy+dy[d]
        nextx = tempx+dx[d]

        if 0<=nexty<N and 0<=nextx<N and arr[nexty][nextx]!=0 and not visited[nexty][nextx]: 
            DFS(nexty, nextx)

def sort(yy,xx):
    global anwlist
    if not anwlist:
        anwlist+=[yy,xx]
        return
    else:
        now = yy*xx
        for k in range(0,len(anwlist),2):
            size = anwlist[k]*anwlist[k+1]
            if now<size:
                anwlist.insert(k, xx)
                anwlist.insert(k, yy)
                break
            elif now == size:
                if anwlist[k]>yy:
                    anwlist.insert(k, xx)
                    anwlist.insert(k, yy)
                    break
            if k==len(anwlist)-2:
                anwlist+=[yy,xx]
                break
                

tcase = int(input())
for tc in range(tcase):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    anwlist=[]
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    count = 0

    for y in range(N):
        for x in range(N):
            if arr[y][x]!=0 and not visited[y][x]: 
                maxx=0
                maxy=0
                firsty = y
                firstx = x
                DFS(y,x)
                #print(firsty, firstx, maxy, maxx)
                count += 1
                #print(maxy-firsty+1, maxx-firstx+1)
                sort(maxy-firsty+1, maxx-firstx+1)

    print('#{} {} '.format(tc+1, count), end='')
    print(*anwlist)
    