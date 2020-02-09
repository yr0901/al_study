dnum=int(input())
dlist=[list(map(int, input().split())) for _ in range(dnum)]
mlist=[[[k[0],k[5]], [k[1], k[3]], [k[2], k[4]]] for k in dlist]