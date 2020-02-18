#줄세우기
stu=int(input())
tlist=[]
clist=list(map(int, input().split()))

for i in range(stu):
    change = clist[i]
    tlist.insert(i-change,i+1)
print(*tlist)