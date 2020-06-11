#어디에 단어가 들어갈 수 있을까
import sys

sys.stdin=open('input.txt', 'r')

tcase = int(input())
for tc in range(tcase):
    N, K = map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    hmat=[[0 for _ in range(N)] for _ in range(N)]

    for y in range(N):#자료 뒤집기
        for x in range(N):
            hmat[x][y]=arr[y][x]

    cnt=0
    for y in range(N):
        for x in range(N-K+1):
            xx = x
            while xx<N and arr[y][xx]==1:
                arr[y][xx]=0
                xx+=1
            if xx-x==K:
                cnt+=1
    for y in range(N):
        for x in range(N - K + 1):
            xx = x
            while xx < N and hmat[y][xx] == 1:
                hmat[y][xx] = 0
                xx += 1
            if xx - x == K:
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))



