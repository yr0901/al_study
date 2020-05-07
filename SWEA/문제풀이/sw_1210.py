#Ladder1
import sys
sys.stdin = open('input.txt', 'r')

def ispossible(y,x):
    if y>=0 and y<100 and x>=0 and x<100 and arr[y][x] ==1 : return True

def ladder(y,x):

    dx=[1,-1,0]
    dy=[0,0,-1]
    arr[y][x]=-1
    global anw

    if y==0:
        anw=x
        return

    for dir in range(3):
        newy=y+dy[dir]
        newx=x+dx[dir]

        if ispossible(newy, newx):
            ladder(newy, newx)
            return

for tc in range(1,11):
    input()
    arr=[list(map(int, input().split())) for _ in range(100)]
    anw=0
    k=0
    for i in range(100):
        if arr[99][i]==2:
            k=i
    
    ladder(99,k)
    print('#{} {}'.format(tc,anw))