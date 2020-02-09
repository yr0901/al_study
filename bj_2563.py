#색종이

num=int(input())
arr=[[0 for _ in range(100)] for _ in range(100)]
for n in range(num):
    x,y=map(int, input().split())
    for tx in range(x,x+10):
        for ty in range(y,y+10):
            arr[tx][ty]=1
summ=0
for t in range(100):
    for k in range(100):
        if arr[t][k]==1:
            summ+=1
print(summ)