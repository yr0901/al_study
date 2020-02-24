#블랙잭_백트래킹 버전
N,M = map(int, input().split())
Card = list(map(int, input().split()))
maxn=0
stop=False

for i in range(N-2):
    if stop:
        break
    tsum=Card[i]
    if tsum>=M:
        continue

    for j in range(i+1, N-1):
        if stop:
            break
        tsum=Card[i]+Card[j]
        if tsum>=M:
            continue

        for k in range(j+1, N):
            if stop:
                break
            tsum=Card[i]+Card[j]+Card[k]
            if tsum==M:
                maxn=M
                stop=True
                break
            elif tsum>maxn and tsum<M:
                maxn=tsum
print(maxn)