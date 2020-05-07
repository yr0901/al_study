#노드의 거리
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

def BFS(start, goal):
    q = deque()
    q.append((0,start))

    while q:
        beforen, nown = q.popleft()
        depth = visited[beforen][nown] +1

        for nextn in range(V+1):
            if arr[nown][nextn] and nextn == goal:
                return depth

            if arr[nown][nextn] and not visited[nown][nextn]:
                q.append((nown,nextn))
                visited[nown][nextn] = depth
             
    return 0 

T =int(input())

for tc in range(T):
    V, E = map(int, input().split())
    nlist = [tuple(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    visited = [[0 for _ in range(V+1)] for _ in range(V+1)]

    #인접행렬 만들기
    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for temp in nlist:
        y, x = temp
        arr[y][x] = 1
        arr[x][y] = 1   

    print(f'#{tc+1} {BFS(S,G)}')