tcase = int(input())

for tc in range(tcase):
    n=int(input())
    arr=[[1,1] for _ in range(n)]
    for i in range(n):
        if i==0:
            arr[i].remove(1)

        if i>1:
            for k in range(i-1):
                arr[i].insert(k+1, arr[i-1][k+1]+arr[i-1][k])
    
    
    print('#{}'.format(tc+1))
    for j in arr:
        print(*j)
