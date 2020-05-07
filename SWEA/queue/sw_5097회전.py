#회전

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    tlist = list(map(int, input().split()))
    front = 0

    for m in range(M):
        front = (front+1)%N
    
    print(f'#{t+1} {tlist[front]}')
