#블록맞추기
import sys
sys.stdin=open('input.txt','r')



N = int(input())
u,v,w,x,y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

