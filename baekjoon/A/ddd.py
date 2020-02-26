def block(startx, starty, hlen, wlen):
    for y in range(starty, hlen):
        for x in range(startx, wlen):
            if arr[y][x]==0:


def length(starty, startx,i):
    tlen=1
    while arr[starty+dy[i]][startx+dx[i]]==1 and starty+dy[i]>=0 and startx+dx[i]>=0 and starty+dy[i]<=N and startx+dx[i]<=N:
        tlen+=1
        starty=starty+dy[i]
        startx = startx+dx[i]
    return tlen

N = int(input())
u,v,w,x,y = map(int, input().split())
arr= [list(map(int, input().split())) for _ in range(N)]
dy=[0,1]
dx=[1,0]

for y in range(N):
    for x in range(N):
        if arr[y][x]==1 and arr[y-1][x]==0 and arr[y][x-1]==0:
            startx = x
            starty = y
            for i in range(2):
                if i&1:
                    wlen=length(startx,starty,i)
                else: hlen=length(startx,starty,i)
            starty += hlen
            startx = x
            for i in range(2):
                if i&1:
                    if length(startx,starty,i) > wlen:
                        wlen=length(startx,starty,i)
                else: 
                    if length(startx,starty,i)>hlen:
                        hlen=length(startx,starty,i)
        


            