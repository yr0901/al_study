N, K = map(int, input().split())
tlist=list(map(int, input().split()))
maxn=-12345
for n in range(N-K):
    summ=0
    for k in range(K):
        if tlist[n+k]<0:
            break
        summ+=tlist[n+k]
    if summ>maxn:
        maxn=summ
print(maxn)