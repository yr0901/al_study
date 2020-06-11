#숫자 배열 회전
import sys
sys.stdin=open('input.txt','r')

tcase=int(input())
for tc in range(tcase):
    N=int(input())
    arr=[list(input().split()) for _ in range(N)]
    new=[[0 for _ in range(N)] for _ in range(N)]
    anwlist=[]
    for n in range(3):
        for x in range(N): #90도 돌리기
            for y in range(N):
                new[x][N-1-y]=arr[y][x]

        for temp in new:
            anwlist.append(''.join(temp))
        arr=new
        new = [[0 for _ in range(N)] for _ in range(N)]

    print('#{}'.format(tc + 1))
    for k in range(N):
        for i in range(len(anwlist)):
            if i%N==k:
                print(anwlist[i], end=' ')
        print()








