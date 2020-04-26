
def makeSome(tempy, tempx, dir, gener):
    #0세대 표시
    tlist = [(tempy, tempx), (tempy+dy[dir],tempx+dx[dir])]

    for i in range(gener):
        ay, ax = tlist[-1]
        if ay-tempy < 0 : tlist.append()
        if ay-tempy > 0 :
        if ax-tempx < 0 :
        if ax-tempx > 0 :


N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]
dy = [0,-1,0,1]
dx = [1,0,-1,0]

for _ in range(N):
    x,y,d,g = map(int,input().split())

    makeSome(y,x,d,g)




