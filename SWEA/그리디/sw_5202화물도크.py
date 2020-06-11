#화물도크

T = int(input())
for tc in range(T):
    N = int(input())
    tlist = [list(map(int, input().split())) for _ in range(N)]
    temp = sorted(tlist, key = lambda x:x[1])
    count = 1
    now = 0
    n = 1 
    while n < len(temp):
        if temp[n][0] < temp[now][1]: n += 1
        else: 
            count += 1
            now = n
            n+=1 
    print(f'#{tc+1} {count}')