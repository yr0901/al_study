#미로의 거리
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')

def BFS(starty, startx):
    q = deque()
    q.append((starty, startx))
    visited[starty][startx] = 0
    depth = 0
    while q:
        nowy, nowx = q.popleft()
        depth = visited[nowy][nowx] + 1 
        for d in range(4):
            nexty = nowy + dy[d]
            nextx = nowx + dx[d]
            if 0<=nexty<N and 0<=nextx<N and not visited[nexty][nextx] and arr[nexty][nextx] == 0:
                q.append((nexty, nextx))
                visited[nexty][nextx] = depth
            elif 0<=nexty<N and 0<=nextx<N and not visited[nexty][nextx] and arr[nexty][nextx] == 3:
                return depth-1
    return 0
    

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited =[[0 for _ in range(N)] for _ in range(N)] 
    dy = [-1,1,0,0]
    dx = [0,0,1,-1]

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                print(f'#{tc+1} {BFS(y, x)}')