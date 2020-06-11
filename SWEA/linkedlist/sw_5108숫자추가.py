#숫자추가

T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())
    tlist = list(map(int, input().split()))
    for m in range(M):
        idx, num = map(int, input().split())
        tlist.insert(idx, num)
    
    print(f'#{tc+1} {tlist[L]}')
    
