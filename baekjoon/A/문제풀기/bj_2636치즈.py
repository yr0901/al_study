#치즈
import sys
sys.setrecursionlimit(10**6)

def DFS(tempy, tempx):

    visited[tempy][tempx]=True

    for d in range(4):
        nexty = tempy + dy[d]
        nextx = tempx + dx[d]
        if isSafe(nexty, nextx) and arr[nexty][nextx] ==1: arr[nexty][nextx] = 2

    for d in range(4):
        nexty = tempy + dy[d]
        nextx = tempx + dx[d]
        if isSafe(nexty, nextx) and arr[nexty][nextx] ==0 and not visited[nexty][nextx]: DFS(nexty, nextx)

def isSafe(nexty, nextx):
    if 0<=nexty<N and 0<=nextx<M:
        return True
    return False        

def MeltCount():
    count =0
    for y in range(N):
        for x in range(M):
            if arr[y][x]==2: arr[y][x]=0
            if arr[y][x]==1: count+=1
    return count

N,M= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
case=0
count = MeltCount()
while True:
    before = count
    # for k in arr:
    #     print(k)
    # print()

    visited=[[False for _ in range(M)] for _ in range(N)]
    DFS(0,0)

    count = MeltCount()
    case +=1

    if count==0:
        break

print(case)
print(before)