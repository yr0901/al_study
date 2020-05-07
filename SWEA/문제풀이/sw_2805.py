#농작물 수확하기
import sys
sys.stdin=open('input.txt','r')

tcase = int(input())

for tc in range(tcase):
    size=int(input())
    arr=[list(map(int, list(input()))) for _ in range(size)]


    start=size//2
    end=size//2
    sum=0
    line=0

    for t in range(size):
        temp = arr[t]
        for i in range(start, end+1):
            sum+=temp[i]

        line += 1
        if line<=size//2:
            start-=1
            end+=1
        else:
            start+=1
            end-=1

    print('#{} {}'.format(tc+1, sum))