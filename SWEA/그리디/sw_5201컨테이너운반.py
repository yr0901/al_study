#컨테이너운반

T = int(input())
for tc in range(T):
    #N개의 컨테이너, M개의 트럭
    N, M = map(int, input().split())
    nlist = list(map(int, input().split()))
    mlist = list(map(int, input().split()))

    nlist.sort(reverse=True)
    mlist.sort(reverse=True)

    container = 0
    anw = 0

    for truck in mlist:
        while container < len(nlist) and truck < nlist[container]:
            container += 1
        if container >= len(nlist):
            break
        anw += nlist[container]
        container += 1

    print(f'#{tc+1} {anw}')