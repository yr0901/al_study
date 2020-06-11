import sys
sys.stdin=open('input.txt','r')

def DFS(here):
    print(here)
    visited[here]=True

    for next in range(0,howmany):
        if mymap[here][next] and not visited[next]:
            DFS(next)

data = list(map(int, input().split()))
howmany = len(data)>>1
mymap =[[0]*howmany for i in range(howmany)]
visited=[0]*8

for i in range(howmany):
    start = data[i*2]
    stop = data[i*2+1]
    mymap[start][stop]=1
    mymap[stop][start]=1
    