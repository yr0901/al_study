#벽 부수고 이동하기
from collections import deque

def BFS(nowy, nowx, depth):
    global BOOM, minn
    deq = deque()
    deq.append((nowy, nowx, depth,BOOM))
    visited[nowy][nowx] = True

    while deq:
        nowy, nowx, depth, BOOM= deq.popleft()

        if nowy == N-1 and nowx == M-1:
            if minn > depth:
                minn = depth
        
        elif depth > minn:
            continue

        for d in range(4):
            nexty = nowy + dy[d]
            nextx = nowx + dx[d]

            if 0<=nexty<N and 0<=nextx<M and not visited[nexty][nextx]:
                if arr[nexty][nextx] == 1 and BOOM:
                    BOOM = False

                    deq.append((nexty,nextx,depth+1,BOOM))
                    visited[nexty][nextx] = True
                    
                    BOOM = True

                elif arr[nexty][nextx] == 0:
                    deq.append((nexty, nextx, depth+1,BOOM))
                    visited[nexty][nextx] = True


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dy = [0,0,1,-1]
dx = [1,-1,0,0]
minn = 987654321
BOOM = True

BFS(0,0,1)

if minn == 987654321:
    minn = -1

print(minn)