#감시
def makeSome(n,anw):
    global visited, maxx

    if n > len(CCTV)-1:
        if anw > maxx:
            maxx = anw
        return
            
    starty, startx = CCTV[n]
    num = arr[starty][startx]
    nowCCTV = direction[num-1]
    for dir in range(len(nowCCTV)):
        count = 0
        temp = []
        for d in nowCCTV[dir]:
            nowy = starty
            nowx = startx
            while True:
                nexty = nowy + dy[d]
                nextx = nowx + dx[d]
                if 0<=nexty<N and 0<=nextx<M and arr[nexty][nextx] != 6:
                    if arr[nexty][nextx] == 0 and not visited[nexty][nextx] :
                        #print(nexty, nextx)
                        count+=1
                        visited[nexty][nextx] = 1
                        temp.append((nexty, nextx))
                    nowy = nexty
                    nowx = nextx
                else: break

        makeSome(n+1, anw+count)

        for y, x in temp:
            visited[y][x] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

#1번: 하나씩 | 2번: (0,2), (1,3) | 3번: (0,1)(1,2)(2,3)(3,0)| 4번: (0,1,2)(1,2,3)(0,2,3)(0,1,3) | 5번 : 전부
dx = [1,0,-1,0]
dy = [0,1,0,-1]
direction = [[[0],[1],[2],[3]], [[0,2],[1,3]], [[0,1],[1,2],[2,3],[3,0]], [[0,1,2],[1,2,3],[0,2,3],[0,1,3]], [[0,1,2,3]]]
visited=[[0 for _ in range(M)] for _ in range(N)]
maxx =-1

CCTV=[]
notzero = 0
#cctv 찾기
for y in range(N):
    for x in range(M):
        if arr[y][x]:
            notzero += 1
            if arr[y][x] != 6:
                CCTV.append((y,x))
         

makeSome(0,0)
print(N*M - maxx - notzero)