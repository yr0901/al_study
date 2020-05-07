#미로1
import sys

sys.stdin=open('input.txt','r')

for i in range(10):
    tcase=int(input())
    arr=[list(map(int, input().split())) for _ in range(16)]
    dy=[1,-1,0,0]
    dx=[0,0,1,-1]
    stack=[(1,1)]
    visited=[[0 for _ in range(17)] for _ in range(17)]
    visited[1][1]=1
    t=False

    while stack:
        if t:
            break

        y,x = stack.pop()

        for d in range(4):
            nexty=y+dy[d]
            nextx=x+dx[d]

            if arr[nexty][nextx]==3:
                break

            if arr[nexty][nextx]==0 and visited[nexty][nextx]!=1:
                y=nexty
                x=nextx
                stack.append((y,x))

            else:
                y,x=stack.pop()








