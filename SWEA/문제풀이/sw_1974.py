#스도쿠 검증
import sys
sys.stdin=open('input.txt','r')
tcase = int(input())

for tc in range(tcase):
    sdk=[list(map(int, input().split())) for _ in range(9)]
    anw=1

    for y in range(9):
        xsum = 0
        for x in range(9):
            if sum(sdk[y])!=45:
                anw=0
            xsum+=sdk[x][y]
        if xsum!=45:
            anw=0
    i=0
    while i<9:
        dsum=0
        for y in range(i,i+3):
            for x in range(i, i+3):
                dsum+=sdk[y][x]
        if dsum!=45:
            anw=0
        i+=3


    print('#{} {}'.format(tc+1, anw))
