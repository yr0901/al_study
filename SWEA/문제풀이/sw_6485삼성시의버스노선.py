#삼성시의 버스노선
tcase = int(input())
for tc in range(tcase):
    N = int(input())
    ablist = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    clist = [int(input()) for _ in range(P)]
    anwlist = [0]*5001

    for n in range(N):
        temp = ablist[n]
        for k in range(temp[0], temp[1]+1):
            anwlist[k]+=1

    print('#{}'.format(tc+1), end=' ')
    for t in clist:
        print(anwlist[t], end=' ')
    print()
        