#백트래킹을 이용한 부분집합 구하기
def backtrack(a,k,input):
    #global MAXCANDIDATES
    c=[1,0]

    if k==input:
        for i in range(1,input+1):
            if a[i]==True:
                print(i, end=' ')
        print()
    else:
        k+=1

        for i in range(2):
            a[k]=c[i]
            backtrack(a,k,input)

#MAXCANDIDATES=100
NMAX=100
a=[0]*NMAX
backtrack(a,0,3)#원하는 부분집합의 길이 : 3

############################################
#백트래킹를 이용한 부분집합 개수 구하기

def getpowerset(a,k,s):
    global count, num
    
    if k==num:
        for n in range(k):
        count+=1
        return
    else:
        k+=1
        for i in range(2):
            a[k]=k
            getpowerset(a,k,s+k)



num=int(input())
a=[0]*(num+1)
count=k=s=0
getpowerset(a,k)

print(count)