#그래프 경로
import sys

sys.stdin=open('input.txt','r')

def graph(s,g):

    global visited,anw
    if 1 not in arr[s]:#필요없음
        return

    for k in range(V+1):
        if arr[s][k]==1 and visited[k]==0:
            if k==g:
                anw=True
                return
            else:
                visited[k]=1
                graph(k,g)

tcase = int(input())

for tc in range(tcase):
    V, E = map(int, input().split())
    visited=[0 for _ in range(V+1)]
    arr=[[0 for _ in range(V+1)] for _ in range(V+1)]
    anw=False

    for e in range(E):
        x,y=map(int, input().split())
        arr[x][y]=1

    s,g = map(int, input().split())

    graph(s,g)

    if anw:
        anw=1
    else: anw=0

    print('#{} {}'.format(tc+1, anw))

#----------------------------------------------
#승민오빠 풀이
TCs = int(input())

def dfs(start,end):
    stack = []
    stack.append(start)
    visit[start] = 1

    while stack:
        now = stack.pop()

        for next in graph[now]:
            if visit[next]:
                continue
            if next == end:
                return 1
            stack.append(next)
            visit[next] = 1
    return 0
for tc in range(TCs):
    v,e = map(int,input().split())

    graph = [[] for _ in range(v+1)]
    visit = [0 for _ in range(v+1)]
    for _ in range(e):
        start, end = map(int,input().split())

        graph[start].append(end)

    start, end = map(int,input().split())

    print('#%d %d'%((tc+1),dfs(start,end)))


