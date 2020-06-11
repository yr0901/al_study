#이진 탐색
def BinarySearch(num, start, end, flag):
    count = 0
    while True:
        center = (start+end) // 2

        if nlist[center] < num and flag != 'right':
            start = center+1
            flag = 'right'
            continue

        elif nlist[center] > num and flag != 'left':
            end = center-1
            flag = 'left'
            continue
        
        elif nlist[center] == num:
            count += 1
            break
        
        break

    return count
    
T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    nlist = list(map(int, input().split()))
    mlist = list(map(int, input().split()))
    anw = 0
    nlist.sort()
    for now in mlist:
        anw += BinarySearch(now, 0, N-1, 'start')
    print(f'#{tc+1} {anw}')
