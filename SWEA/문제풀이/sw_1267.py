#작업 순서

for tcase in range(1):
    V, E =map(int, input().split())
    tlist=list(map(int, input().split()))
    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    indegree = [0 for _ in range(V+1)]
    outdegree = [0 for _ in range(V+1)]

    i=0
    while i<=(2*V)-1: 
        outdegree[tlist[i]]+=1
        indegree[tlist[i+1]]+=1
        i+=2    
    
    for k in range(len(tlist)-1):
        arr[tlist[k]][tlist[k+1]]+=1
# [0, 1, 1, 1, 0, 2, 2, 1, 0, 1]
# [0, 2, 2, 0, 1, 1, 0, 1, 2, 0]
    t=1
    temp=0
    next=0
    anwlist=[]
    while True:
        if indegree[t]==0 and outdegree[t]!=0: 
            print('!')
            temp=t
            for k in range(V+1):
                if arr[temp][k]==1:
                    anwlist.append(temp)
                    next=k
                    break
            outdegree[temp]-=1
            indegree[next]-=1
            temp=next
        
        if sum(indegree)==0 and sum(outdegree)==0:
            break
        t+=1
    print(anwlist)
    

            



    