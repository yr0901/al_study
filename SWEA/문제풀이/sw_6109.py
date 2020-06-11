#추억의 2048게임
import sys
sys.stdin = open('input.txt','r')

tcase = int(input())
for tc in range(tcase):
    N, dir = input().split()
    N=int(N)
    arr=[list(map(int, input().split())) for _ in range(int(N))]
    xstart=[0, 0, 0, N-1]
    ystart=[0, N-1, 0, 0]
    d=[1,-1]
    anwlist=[]

    if dir=='up':
        x=0
        while x<N:
            tlist=[]
            y=0
            while y<N:
                if arr[y][x]!=0:
                    tlist.append(arr[y][x])
                y+=1
            x+=1
            t=0
            new = []

            while t<=len(tlist)-1:
                if t==len(tlist)-1:
                    new.append(tlist[t])
                    t+=1

                elif tlist[t]==tlist[t+1]:
                    new.append(tlist[t]*2)
                    t+=2
                else:
                    new.append(tlist[t])
                    t+=1
            anwlist.append(new)
    if dir=='down':
        x = 0
        while x<N:
            tlist=[]
            y = N - 1
            while y<N:
                if arr[y][x]!=0:
                    tlist.append(arr[y][x])
                y-=1
            x+=1
            t=0
            new = []

            while t<=len(tlist)-1:
                if t==len(tlist)-1:
                    new.append(tlist[t])
                    t+=1

                elif tlist[t]==tlist[t+1]:
                    new.append(tlist[t]*2)
                    t+=2
                else:
                    new.append(tlist[t])
                    t+=1
            anwlist.append(new)
    if dir=='left':
        y=0
        while y<N:
            tlist=[]
            x=0
            while x<N:
                if arr[y][x]!=0:
                    tlist.append(arr[y][x])
                y+=1
            x+=1
            t=0
            new = []

            while t<=len(tlist)-1:
                if t==len(tlist)-1:
                    new.append(tlist[t])
                    t+=1

                elif tlist[t]==tlist[t+1]:
                    new.append(tlist[t]*2)
                    t+=2
                else:
                    new.append(tlist[t])
                    t+=1
            anwlist.append(new)

    if dir=='right':
        y=0
        while y<N:
            tlist=[]
            x=N-1
            while x<N:
                if arr[y][x]!=0:
                    tlist.append(arr[y][x])
                y+=1
            x+=-1
            t=0
            new = []

            while t<=len(tlist)-1:
                if t==len(tlist)-1:
                    new.append(tlist[t])
                    t+=1

                elif tlist[t]==tlist[t+1]:
                    new.append(tlist[t]*2)
                    t+=2
                else:
                    new.append(tlist[t])
                    t+=1
            anwlist.append(new)
    if dir=='up':
        while x<N:
            tlist=[]
            y=ystart[0]
            while y<N:
                if arr[y][x]!=0:
                    tlist.append(arr[y][x])
                y+=d
            x+=d
            t=0
            new = []

            while t<=len(tlist)-1:
                if t==len(tlist)-1:
                    new.append(tlist[t])
                    t+=1

                elif tlist[t]==tlist[t+1]:
                    new.append(tlist[t]*2)
                    t+=2
                else:
                    new.append(tlist[t])
                    t+=1
            anwlist.append(new)

    print(anwlist)
