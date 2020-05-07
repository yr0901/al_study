#겹치는 면적 구하기

tc = int(input())
for tcase in range(tc):
    num=int(input())
    arr=[[0]*15 for _ in range(15)]
    
    count=0
    for i in range(num):
        temp=list(map(int, input().split()))
        for x in range(temp[0],temp[2]+1):
            for y in range(temp[1],temp[3]+1):
                if arr[x][y] ==0:
                    arr[x][y]=temp[-1] #색
                else :
                    count+=1

    print(f'#{tcase+1} {count}')     