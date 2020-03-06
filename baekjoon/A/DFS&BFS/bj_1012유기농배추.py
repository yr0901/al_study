#유기농 배추
def BFS(nowy, nowx):
    queue = [(nowy, nowx)]
    arr[nowy][nowx] = 2

    while queue:
        # print(queue)
        nowy, nowx = queue.pop(0)
        arr[nowy][nowx] = 2

        for d in range(4):
            nexty = nowy + dy[d]
            nextx = nowx + dx[d]
            if 0<=nexty<N and 0<=nextx<M and arr[nexty][nextx] == 1:
                queue.append([nexty, nextx])
                arr[nexty][nextx] = 2
        
T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    tlist = [list(map(int, input().split())) for _ in range(K)]
    arr = [[0 for _ in range(M)] for _ in range(N)]
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    count = 0

    for tt in tlist:
        arr[tt[1]][tt[0]] = 1

    for y in range(N):
        for x in range(M):
            if arr[y][x]==1: 
                BFS(y,x); 
                count+=1
    print(count)