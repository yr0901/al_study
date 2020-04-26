#아기상어
from collections import deque

def BFS(starty, startx, size, ate, count):
    global visited

    q =deque()
    q.append((starty, startx, size, ate, count))
    anw = 0
    nextc = 0
    temp = []

    while q:
        nowy, nowx, size, ate, nowc = q.popleft()

        if nowc == nextc and temp:
            #print(temp)
            temp.sort()
            #print(temp)
            nexty, nextx, size, ate, count = temp[0]
            temp = []
            arr[nexty][nextx] = 0
            ate += 1
            anw += count
            #print(anw)
            
            visited = [[0 for _ in range(N)] for _ in range(N)]
            visited[nexty][nextx] = 1
            q.clear()
            q.append((nexty, nextx, size, ate, 0))
            continue

        if ate == size:
            size += 1
            ate = 0

        for d in range(4):
            nexty = nowy + dy[d]
            nextx = nowx + dx[d]
            
            if 0<=nexty<N and 0<=nextx<N and not visited[nexty][nextx]:
                if 0< arr[nexty][nextx] < size:
                    visited[nexty][nextx] = 1
                    nextc = nowc + 1
                    temp.append((nexty, nextx, size, ate, nextc))

                elif arr[nexty][nextx] == size or arr[nexty][nextx] == 0:
                    visited[nexty][nextx] = 1
                    nextc = nowc + 1
                    q.append((nexty, nextx, size, ate, nextc))
        if temp and not q:
            temp.sort()
            #print(temp)
            nexty, nextx, size, ate, count = temp[0]
            temp = []
            arr[nexty][nextx] = 0
            ate += 1
            anw += count
            #print(anw)
            
            visited = [[0 for _ in range(N)] for _ in range(N)]
            visited[nexty][nextx] = 1
            q.clear()
            q.append((nexty, nextx, size, ate, 0))
    return anw

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
dy = [-1,0,0,1]
dx = [0,-1,1,0]
count = 0
#아기상어 찾기
for y in range(N):
    for x in range(N):
        if arr[y][x] == 9:
            arr[y][x] = 0
            visited[y][x] = 1
            print(BFS(y,x,2,0,0))
            break