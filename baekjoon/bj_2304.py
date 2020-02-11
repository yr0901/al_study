#창고 다각형

N= int(inptu())
tlist=[map(int, input().split()) for _ in range(N)]
tlist.sort()

maxx=0
maxh=h

for i in range(len(tlist)):
    if tlist[1]>maxh:
        maxh=tlist[1]
        maxx=tlist[0]

area=0
k=0
while k<maxx:
    for d in range(1,len(tlist)-1):
        temph=tlist[k][1]
        tempx=tlist[k][0]
        nexth=tlist[k+d][1]
        nextx=tlist[k+d][0]
        if temph>nexth:
            area+=temph*(nextx-tempx)
            break
    k+=d

while k>maxx:
    temph=tlist[N][1]
    tempx=tlist[N][0]
    nexth = tlist[N - k][1]
    nextx = tlist[N - k][0]







