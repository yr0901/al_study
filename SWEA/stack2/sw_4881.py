import sys
sys.stdin=open('input.txt','r')
myMin = None
def getnext(y,x,summ,xlist):
    global myMin
    summ+=arr[y][x]
    xlist.append(x)
    if y==N-1:
        if myMin>summ:
            myMin=summ
        return

    for next in range(N):
        if summ>myMin:
            break
        if next not in xlist:
            getnext(y+1,next,summ,xlist)
            xlist.pop()


tcase=int(input())
for tc in range(tcase):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    myMin=987654321

    for i in range(N):
        xlist=[]
        getnext(0,i,0,xlist)

    print('#{} {}'.format(tc+1,myMin))


            
            