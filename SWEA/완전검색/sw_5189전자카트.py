#전자카트
import sys
sys.stdin = open('input.txt', 'r')

def DFS(now, nowsum, depth):
    global minn,N

    if depth == N-1:
        nowsum += arr[now][0]
        if nowsum < minn:
            minn = nowsum
        return

    for n in range(1, N):
        if arr[now][n] and not visited[n] and nowsum + arr[now][n] < minn:
            visited[now] = 1
            DFS(n, nowsum + arr[now][n], depth+1)
            visited[now] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    #visited = [[0 for _ in range(N)] for _ in range(N)]
    minn = 987654321
    DFS(0, 0, 0)

    print(f'#{tc+1} {minn}')