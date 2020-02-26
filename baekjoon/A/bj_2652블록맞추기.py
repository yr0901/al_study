#블록맞추기
import sys
sys.stdin=open('input.txt','r')

def block(arr):
    for y in range(N):
        for x in range(N):
            if arr[y][x]==1:
                sidx = x
                while arr[y][x]==1:
                    fidx=x
                    x+=1
                if sidx==fidx
                return sidx, fidx


N = int(input())
u,v,w,x,y = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
#arr2 = zip(*arr1)

 block(arr1)

