#참외밭
<<<<<<< HEAD
melon=int(input())
tlist=[]
drlist=[]
kmlist=[]
maxlist=[]
minlist=[]

for n in range(6):
    dr, km = map(int, input().split())
    drlist.append(dr)
    kmlist.append(km)

for i in range(6):
    if drlist.count(drlist[i])==1:
        maxlist.append(kmlist[i])
    else:
        minlist.append(kmlist[i])
max=min=1
for k in range(2):
    max*=maxlist[k]

for t in range(4):
    if t==1 or t==2:
        min*=minlist[t]

print((max-min)*melon)
    
=======
km=int(input())

#동:1 서:2 남:3 북:4
x,y=0,0
#arr = [[0 for _ in range(500)] for _ in range(500)]
tlist=[list(map(int, input().split())) for _ in range(6)]

maxx=maxy=maxydir=maxxdir=0

for i in range(6):
    dir=tlist[i][0]
    kilo=tlist[i][1]

    if dir==4 or dir==3 and kilo>maxy:
        maxy=kilo
        maxydir=dir

    elif dir==1 or dir==2 and kilo>maxx:
        maxx=kilo
        maxxdir=dir


>>>>>>> dfb2e8f8d1eb80de2d0643043148fc24335ddf8c



        

