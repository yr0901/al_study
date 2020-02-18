N, K = map(int, input().split())
tlist=list(map(int, input().split()))
maxn=-12345
summ=0
for i in range(0,K):
    summ+=tlist[i]
if summ>maxn:
    maxn=summ
n=0
while n<=N-K-1:
    summ=summ-tlist[n]+tlist[n+K]
    if summ>maxn:
        maxn=summ
    n+=1

print(maxn)