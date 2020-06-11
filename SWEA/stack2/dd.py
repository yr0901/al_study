#백트래킹을 이용하여 순열 구하기
import sys
sys.stdin=open('input.txt','r')

def getsome(tstring, k):
    if k==3:
        if tstring[k]!=0:
            print(string[k-1])
    else:
        k+=1
        tstring[k]=k
        getsome(tstring, k)

string=list(input())
tstring=[0]*(len(string)+1)
k=0
getsome(tstring, k)
'''''''''''''''''''''''''''
'''''''''''''''''''''''''''
def perm_r_1(a,k,N):
    if k ==N:
        print(a)
    else:
        in_perm=[False]*N
        c=[0]*N

        for i in range(k):
            in_perm[a[i]]=True
        
        ncandidates=0
        for i in range(N):
            if in_perm[i]==False:
                c[ncandidates]=i
                ncandidates+=1
        for i in range(ncandidates):
            a[k]=c[i]
            perm_r_1(a,k+1,N)
