#종이의 개수
import sys

sys.stdin = open('input.txt','r')

def CHECK(N, starty, startx, cut):
    global c
    num = N//cut
    if num == 0:
        num = 1

    for sy in range(0,N,num):
        for sx in range(0, N, num):
            stop=False
            if starty+sy >= N or startx+sx >= N:
                break
            default = arr[starty+sy][startx+sx]
            #print(starty, startx, sy, sx)
            for y in range(num):
                for x in range(num):
                    if stop:
                        break
                    nexty = starty+sy+y
                    nextx = startx+sx+x
                    if 0<=nexty<N and 0<=nextx<N and arr[nexty][nextx] != default:
                        CHECK(N, starty+sy, startx+sx, cut*3)
                        stop = True
                if stop:
                    break
            if not stop:    
                count[default+1] += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
count= [0] * 3
c = 0
CHECK(N,0,0,1)

for t in count:
    print(t)