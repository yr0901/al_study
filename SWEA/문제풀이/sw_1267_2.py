#작업순서
# def DFS():
def issafe(nexty):
    for n in range(V):
        if arr[n][nexty]==1:
            return False, n
    return True, nexty

def DFS(y):
    anw=[]
    if count==E:
        anw.append(y)
        return
    if 1 not in arr[y]:
        return
    for k in range(V): #선행과제 수행 여부 확인
        if arr[k][y]==1:
            return
    for x in range(V):
        if x==1:
            arr[y][x]=-1
            TF, n = issafe(x)
            if TF:
                nexty=x
            else:
                nexty=n
            DFS(nexty)
            
        anw.append(y)
        return
        


for tcase in range(1):
    V, E =map(int, input().split())
    tlist=list(map(int, input().split()))
    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    i=0

    while i<= range(E-1):
        arr[tlist[i]][tlist[i+1]] =1
        i+=2

    for i in range(V):
        if arr

