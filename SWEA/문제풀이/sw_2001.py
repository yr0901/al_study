#파리퇴치

import sys
sys.stdin = open('input.txt','r')

tcase=int(input())

for tc in range(tcase):
    N, M =map(int,input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    maxn=0

    for i in range(N-M):
        for h in range(N-M):
            sum=0
            for k in range(M):
                for t in range(M):
                    sum+=arr[i+k][h+t]
            
            if maxn<sum:
                maxn=sum

    print('#{} {}'.format(tc+1, maxn))

    