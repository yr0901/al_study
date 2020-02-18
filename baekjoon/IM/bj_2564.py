#경비원
w, h = map(int, input().split())
howmany = int(input())
ansum=0
dlist=[]
for _ in range(howmany+1):
    x,y=map(int, input().split())
    if x==1:
        dlist.append([0,y])
    elif x==2:
        dlist.append([h,y])
    elif x==3:
        dlist.append([y,0])
    else:
        dlist.append([y,w])

dx=dlist[howmany][0]
dy=dlist[howmany][1]

for n in range(howmany):
    if dlist[n][0]==dx:
        anw=abs(dy-dlist[n][1])
    elif dlist[n][0]!=dx and abs(dlist[n][0]-dx)<h:
        anw=abs(dy-dlist[n][1]) + abs(dx-dlist[n][0])
    else: 
        if dy + dlist[n][1]<=(w-dy) + (w-dlist[n][1]):
            anw = h + dy + dlist[n][1]
        else :
            anw= h+(w-dy) + (w-dlist[n][1])

    ansum+=anw

print(ansum)