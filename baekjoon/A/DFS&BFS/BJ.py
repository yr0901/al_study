#벽 부수고 이동하기
from collections import deque

def BFS(nowy, nowx, depth):
    global BOOM, minn
    deq = deque()
    deq.append((nowy, nowx, depth, BOOM))
    visited[nowy][nowx] = BOOM

    while deq:
        nowy, nowx, depth, BOOM= deq.popleft()

        if nowy == N-1 and nowx == M-1:
            if minn > depth:
                minn = depth

        for d in range(4):
            nexty = nowy + dy[d]
            nextx = nowx + dx[d]

            if 0<=nexty<N and 0<=nextx<M:
                if not visited[nexty][nextx]:
                    if arr[nexty][nextx]==0:
                        deq.append((nexty,nextx,depth+1,BOOM))
                        visited[nexty][nextx] = [BOOM,depth]
                    elif BOOM==1:
                        BOOM *= -1

                        deq.append((nexty,nextx,depth+1,BOOM))
                        visited[nexty][nextx] = [BOOM,depth]
                        
                        BOOM *=-1

                elif visited[nexty][nextx][0] == 1:
                    if BOOM == -1:
                        deq.append((nexty,nextx,depth+1,BOOM))
                        visited[nexty][nextx] = [BOOM,depth]

                elif visited[nexty][nextx][0] == -1 and visited[nexty][nextx][1] => depth+1:
                    deq.append((nexty,nextx,depth+1,BOOM))
                    visited[nexty][nextx] = [BOOM,depth]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
dy = [0,0,1,-1]
dx = [1,-1,0,0]
minn = 987654321
BOOM = 1

BFS(0,0,1)

if minn == 987654321:
    minn = -1

print(minn)