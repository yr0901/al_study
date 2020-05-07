#정곤이의 단조 증가하는 수

tcase=int(input())

def danzo(n):
    if len(str(n))>1:
        for k in range(len(str(n))-1):
            if int(str(n)[k])>int(str(n)[k+1]):
                return False
        return True  
    else:
        return True

for tc in range(tcase):
    N=int(input())
    nlist= list(map(int, input().split()))
    maxn=-1

    for i in range(len(nlist)-1):
        for k in range(i+1, len(nlist)):
            if danzo(nlist[i]*nlist[k]):
                if maxn<nlist[i]*nlist[k]:
                    maxn=nlist[i]*nlist[k]

    print('#{} {}'.format(tc+1, maxn))