#벽 부수고 이동하기
from collections import deque

def BFS(nowy, nowx, depth):
    deq = deque()
    deq.append((nowy, nowx, depth))
    visited[nowy][nowx] = True

    while deq:
        for d in range(4):
            nowy, nowx, depth = deq.leftpop()
            
            if nowy == N-1 and nowx == M-1:
                if minn > depth:
                    minn = depth

            nexty = nowy + dy[d]
            nextx = nowx + dx[d]

            if 0<=nexty<N and 0<=nextx<M:
                if arr[nexty][nextx] == 1 and BOOM:
                    arr[nexty][nextx] = 0
                    BOOM = False
                    continue
                elif arr[nexty][nextx] == 0:
                    deq.append((nexty, nextx, depth))
                    visited.[nexty][nextx] = True
                elif arr[nexty][nextx] == 1 and not BOOM:
                    continue
        depth +=1

N, M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dy = [0,0,1,-1]
dx = [1,-1,0,0]
minn = 987654321
BOOM = True

BFS(0,0,0)