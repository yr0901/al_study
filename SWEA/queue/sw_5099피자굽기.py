def enque():
    q = deque()
    pizza = -1
    for n in range(N):
        q.append(n)
        pizza +=1

    while q:
        now = q.popleft()
        tlist[now] //= 2
        if tlist[now] == 0:
            if pizza == M-1 :
                continue
            else:
                pizza+=1
                q.append(pizza)
        else:
            q.append(now)
            # tlist[now]//=2

    return now+1

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    tlist = list(map(int, input().split()))
    print(f'#{tc+1} {enque()}')