#참외밭
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





        

