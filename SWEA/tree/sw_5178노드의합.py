#노드의 합

def NodeSum(N):
    for i in range(len(tree)-1,-1,-1):
        if tree[i] and i//2 > 0: 
            tree[i//2] += tree[i]

T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for m in range(M):
        x, y = map(int, input().split())
        tree[x] = y
    
    NodeSum(N)

    print(f'#{tc+1} {tree[L]}')
