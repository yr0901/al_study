#최소합
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')

def DFS(nowy, nowx, nowsum):
    global minn

    if nowy == N-1 and nowx == N-1:
        if nowsum <=minn :
            minn = nowsum
        return

    for d in range(2):
        nexty = nowy + dy[d]
        nextx = nowx + dx[d]
        if 0<=nexty<N and 0<=nextx<N and nowsum+arr[nexty][nextx]<minn:
            DFS(nexty, nextx, nowsum+arr[nexty][nextx])

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [0,1]
    dx = [1,0]
    minn = 987654321
    DFS(0,0,arr[0][0])

    print(f'#{tc+1} {minn}')