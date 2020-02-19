import sys
sys.stdin=open('input.txt','r')


#주사위 굴리기
def issafe(y,x):
    if y>=0 and y<=N and x>=0 and x<=M:
        return True

N,M, x,y,K=map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
klist=list(map(int, input().split()))

#남 동 서 북
dx=[0, 1,-1,0]
dy=[1, 0,0,-1]
did=[1,1,-1,-1]
rdice=[0]*3
cdice=[0]*4

idx=1
idy=1
nowx=x
nowy=y

for k in range(K):
    i = klist[k]%4
    #print('i={}'.format(i))
    nexty=nowy+dy[i]
    nextx=nowx+dx[i]
    #print(nexty, nextx)
    #갈 수 있는지
    if issafe(nexty, nextx):
        nowx=nextx
        nowy=nexty
        if i==1 or i==2:#동쪽 서쪽
            if idx+did[i]>2:
                idx=-1
            if idx+did[i]<0:
                idx=3

            bottom=idx+did[i]
            idx+=did[i]
            #숫자 옮겨가기
            if arr[nowy][nowx]==0:
                arr[nowy][nowx]=rdice[bottom]

            elif arr[nowy][nowx]!=0: 
                rdice[bottom] = arr[nowy][nowx]
                arr[nowy][nowx]=0
            cdice[idy]=rdice[bottom]

        else:#북쪽 남쪽
            if idy+did[i]>3:
                idy=-1
            if idy+did[i]<0:
                idy=4
            bottom=idy+did[i]
            idy+=did[i]
            #숫자 옮겨가기
            if arr[nowy][nowx]==0:
                arr[nowy][nowx]=cdice[bottom]

            else:
                cdice[bottom] = arr[nowy][nowx]
                arr[nowy][nowx]=0

            rdice[idx]=cdice[bottom]
    else: 
        print('생략')
        continue

    print(cdice[idy-2])