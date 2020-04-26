#파이프 옮기기
from collections import deque

def Position(prey,prex,nowy,nowx):
    if nowy-prey == 0 and nowx-prex == 1:
        return 0
    elif nowy-prey == 1 and nowx-prex == 0:
        return 1
    else: return 2

def BFS(starty, startx, endy, endx):
    deq = deque()
    deq.append((starty,startx,endy, endx))
    anw = 0

    while deq:
        prey, prex, nowy, nowx = deq.popleft()
        posi = Position(prey, prex, nowy, nowx)

        for d in dir[posi]:
            nexty = nowy + dy[d]
            nextx = nowx + dx[d]
            if d == 0:
                if nexty == N-1 and nextx == N-1:
                    anw += 1
                    break
                elif 0<=nexty<N and 0<=nextx<N-1 and not arr[nexty][nextx]:
                    deq.append((nowy,nowx,nexty,nextx))

            elif d == 1:
                if nexty == N-1 and nextx == N-1:
                    anw += 1
                    break
                elif 0<=nexty<N-1 and 0<=nextx<N and not arr[nexty][nextx]:
                    deq.append((nowy,nowx,nexty,nextx))

            elif d == 2:
                if nexty == N-1 and nextx == N-1:
                    anw += 1
                    break

                if 0<=nexty<N and 0<=nextx<N and not arr[nexty][nextx] and not arr[nexty-1][nextx] and not arr[nexty][nextx-1]:
                    deq.append((nowy,nowx,nexty,nextx))
    return anw 

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [0,1,1]
dx = [1,0,1]
#가로 : 0번쨰 세로 : 1번째 대각선 : 2번째
dir = [[0,2], [1,2], [0,1,2]]

print(BFS(0,0,0,1))
