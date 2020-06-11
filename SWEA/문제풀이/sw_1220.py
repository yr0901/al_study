#magnetic

import sys
sys.stdin=open('input.txt', 'r')

for tc in range(10):
    m=int(input())
    arr = [list(map(int, input().split())) for _ in range(m)]
    count=0

    for x in range(100):
        stack = []
        for y in range(100):
            if arr[y][x]!=0:
                stack.append(arr[y][x])

        for t in range(len(stack)-1):
            if stack[t]==1 and stack[t+1]==2:
                count+=1

    print('#{} {}'.format(tc+1, count))

#'''''''''''''''''''''''''''''''''''''''''''''''
#태웅오빠 풀이
for tc in range(1, 11):
    print(f'#{tc}', end=' ')

    N = int(input())
    B = [list(map(int, input().split())) for _ in range(N)]

    new = [[] for _ in range(N)]
    for c in range(N):
        temp = []
        for r in range(N):
            if B[r][c]:
                temp.append(B[r][c])
        new[c] = temp[:]

    cnt = 0
    for row in new:
        i = 0
        while i < len(row):
            if row[i] == 1:
                i += 1

                for j in range(i, len(row)):
                    if row[j] == 2:
                        cnt += 1
                        i = j + 1
                        break
            else:
                i += 1
    print(cnt)