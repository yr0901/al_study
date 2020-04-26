#파이프 옮기기
from collections import deque

def Position(prey,prex,nowy,nowx):
    if nowy-prey == 0 and nowx-prex == 1:
        return 0
    elif nowy-prey == 1 and nowx-prex == 0:
        return 1
    else: return 2

def DFS(prey, prex, nowy, nowx):
    global anw 

    if nowy == N-1 and nowx == N-1:
        anw += 1
        return

    posi = Position(prey, prex, nowy, nowx)

    for d in dir[posi]:
        nexty = nowy + dy[d]
        nextx = nowx + dx[d]
        if posi == 0:
            if d != 1:
                if 0<=nexty<N-1 and 0<=nextx<N and not arr[nexty][nextx]:
                    DFS(nowy, nowx, nexty, nextx)
            else:
                if 0<=nexty<N and 0<=nextx<N and not arr[nexty][nextx] and not arr[nexty-1][nextx] and not arr[nexty][nextx-1]:
                    DFS(nowy, nowx, nexty, nextx)
        elif posi == 1:
            if d == 0:
                if 0<=nexty<N-1 and 0<=nextx<N and not arr[nexty][nextx]:
                    DFS(nowy, nowx, nexty, nextx)
            elif d == 1:
                if 0<=nexty<N and 0<=nextx<N and not arr[nexty][nextx] and not arr[nexty-1][nextx] and not arr[nexty][nextx-1]:
                    DFS(nowy, nowx, nexty, nextx)
            elif d == 2:
                if 0<=nexty<N and 0<=nextx<N-1 and not arr[nexty][nextx]:
                    DFS(nowy, nowx, nexty, nextx)
        elif posi == 2:
            if d != 1:
                if 0<=nexty<N and 0<=nextx<N-1 and not arr[nexty][nextx]:
                    DFS(nowy, nowx, nexty, nextx)
            else:
                if 0<=nexty<N and 0<=nextx<N and not arr[nexty][nextx] and not arr[nexty-1][nextx] and not arr[nexty][nextx-1]:
                    DFS(nowy, nowx, nexty, nextx)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [1,1,0]
dx = [0,1,1]
#가로 : 0번쨰 세로 : 1번째 대각선 : 2번째
dir = [[1,2], [0,1], [0,1,2]]
anw = 0

DFS(0,0,0,1)

print(anw)