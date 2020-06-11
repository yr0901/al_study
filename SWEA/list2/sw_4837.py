#부분집합 합

tc= int(input())
a =list(range(1,13))

for tcase in range(tc):
    N, K = map(int, input().split())
    count=0

    for i in range(1<<12):
        temp=[]
        for j in range(12):
            if i&(1<<j):
                temp.append(a[j])
        if len(temp)==N and sum(temp)==K:
            count+=1

    print('#{} {}'.format(tcase+1, count))

