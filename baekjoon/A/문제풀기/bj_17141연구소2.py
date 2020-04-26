#연구소 2 
from collections import deque
def BFS(idxlist):
    global minn, N

    temp = [a[:] for a in arr]
    q = deque()

    for i in idxlist:
        q.append(virus[i])
        temp[virus[i][0]][virus[i][1]] = 1

    while q:
        nowy, nowx, depth = q.popleft()
        if depth > minn :
            return
        for d in range(4):
            nexty = nowy + dy[d]
            nextx = nowx + dx[d]
            if 0<=nexty<N and 0<=nextx<N and temp[nexty][nextx] != 1 :
                q.append((nexty,nextx,depth+1))
                temp[nexty][nextx] = 1

    for y in range(N):
        for x in range(N):
            if temp[y][x]==0:
                return

    if depth<minn:
        minn = depth
    
def getIdx(range_start):
    global M 

    if len(idxlist) == M:
        #bfs 호출
        BFS(idxlist)
        return

    for n in range(range_start, len(virus)):
        idxlist.append(n)
        getIdx(n+1)
        idxlist.pop()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [1,-1,0,0]
dx = [0,0,-1,1]
virus=[]
idxlist=[]
minn = 987654321
#바이러스 놓을 수 있는 자리 찾기
for y in range(N):
    for x in range(N):
        if arr[y][x] == 2:
            virus.append((y,x,0))

#자리의 조합 구하기 
getIdx(0)

if minn == 987654321:
    minn = -1

print(minn)