#수열편집

T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    tlist = list(map(int, input().split()))
    for m in range(M):
        temp = input().split()
        if len(temp) == 3:
            flag, idx, num = temp
        else:
            flag, idx = temp

        if flag == 'I':
            tlist.insert(int(idx), num)
        elif flag == 'D':
            del tlist[int(idx)]
        else: tlist[int(idx)] = num
    
    try:
        print(f'#{tc+1} {tlist[L]}')
    except:
        print(f'#{tc+1} -1')