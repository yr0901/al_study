#subtree

def Subtree(root):
    global count

    for i in range(2):
        if tree[root][i] and not visited[root][i]:
            count+=1
            visited[root][i] = 1
            Subtree(tree[root][i])
    return

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    tree = [[0]*2 for _ in range(E+2)]
    visited = [[0]*2 for _ in range(E+2)]
    tlist = list(map(int, input().split()))
    count = 0

    for i in range(0,len(tlist),2):
        if not tree[tlist[i]][0]:
            tree[tlist[i]][0] = tlist[i+1]
        else:
            tree[tlist[i]][1] = tlist[i+1]
        
    Subtree(N)

    print(f'#{tc+1} {count+1}')