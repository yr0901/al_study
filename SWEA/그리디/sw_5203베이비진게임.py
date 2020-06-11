#베이비진게임

T = int(input())
for tc in range(T):
    clist = list(map(int, input().split()))
    alist = []
    blist = []
    anw = 0
    for card in range(12):
        if card&1:
            blist.append(clist[card])
            if blist.count(clist[card]) == 3:
                anw = 2
            else:
                blist.sort()
                n = 0
                while n+2 <= len(blist)-1:
                    if blist[n+1]-blist[n] == 1 and blist[n+2]-blist[n+1]==1:
                        anw = 2
                        break
                    n += 1
        else:
            alist.append(clist[card])
            if alist.count(clist[card]) == 3:
                anw = 1
            else:
                alist.sort()
                n = 0
                while n+2 <= len(alist)-1:
                    if alist[n+1]-alist[n] == 1 and alist[n+2]-alist[n+1]==1:
                        anw = 1
                        break
                    n += 1
        if anw:
            break
    print(f'#{tc+1} {anw}')