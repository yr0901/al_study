#창고 다각형
num=int(input())
tlist=[]

for i in range(num):
    x, y=map(int, input().split())
    tlist.append([x,y])
tlist.sort()
