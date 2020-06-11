#그룹 나누기

T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    mlist = list(map(int, input().split()))
    visited = [1 for _ in range(N+1)]
    tlist = []
    
    for i in range(0, 2*M, 2):
        visited[mlist[i]] = 0
        visited[mlist[i+1]] = 0
        if not len(tlist):
            tlist.append([mlist[i], mlist[i+1]])
        else:
            flag = False
            for team in tlist:
                if mlist[i] in team: 
                    flag = True
                    team.append(mlist[i+1])
                    
                elif mlist[i+1] in team:
                    flag = True
                    team.append(mlist[i])

            if not flag:
                tlist.append([mlist[i], mlist[i+1]])
        # print(tlist)
        # print(visited)
    print(f'#{tc+1} {len(tlist)+sum(visited)-1}')
