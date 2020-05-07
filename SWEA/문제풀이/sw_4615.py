#재미있는 오셀로 게임
import sys

sys.stdin=open('input.txt', 'r')

tcase = int(input())

def game(tempx, tempy,color, arr):
    dx=[-1,0,1,0,1,-1,1,-1]
    dy=[0,1,0,-1,1,-1,-1,1]

    arr[tempx][tempy]=color #놓기
    for i in range(8):
        k=1
        while tempx +dx[i]*k>=0 and tempx+dx[i]*k<len(arr) and tempy +dy[i]*k>=0 and tempy+dy[i]*k<len(arr):
            if arr[tempx+dx[i]*k][tempy+dy[i]*k]!=0 and arr[tempx+dx[i]*k][tempy+dy[i]*k]!=arr[tempx][tempy]:
                k+=1
            elif arr[tempx+dx[i]*k][tempy+dy[i]*k]==arr[tempx][tempy]:
                k+=1
                break
            else:
                break
        if k>2 and arr[tempx+dx[i]*(k-1)][tempy+dy[i]*(k-1)]==arr[tempx][tempy]:
            for ch in range(1,k):
                if color==1:
                    arr[tempx+dx[i]*ch][tempy+dy[i]*ch] = 1
                else:
                    arr[tempx+dx[i]*ch][tempy+dy[i]*ch] = 2
    return arr

for tc in range(tcase):
    N, M= map(int, input().split())
    glist = [list(map(int, input().split())) for _ in range(M)]
    arr = [[0 for _ in range(N+1)] for _ in range(N+1)] 
    arr[N//2][N//2]=2
    arr[N//2][N//2+1]=1
    arr[N//2+1][N//2]=1
    arr[N//2+1][N//2+1]=2

    for r in range(M):
        tempx=glist[r][0]
        tempy=glist[r][1]
        color=glist[r][2]#b=1 w=2
        game(tempx, tempy, color, arr)
    
    bcount=0
    wcount=0
    for n in arr:
        bcount+=n.count(1)
        wcount+=n.count(2)

    print(f'#{tc+1} {bcount} {wcount}')
            
            

