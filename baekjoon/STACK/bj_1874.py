#스택 수열
n=int(input())
anwlist=[int(input()) for _ in range(n)]
tlist=list(range(2,n+1))
stack=[1]
i=j=0
alist=['+']
anw=True

while stack:
    goal=anwlist[j]
    if stack[-1]<goal:
        stack.append(tlist[i])
        print(stack)
        alist.append('+')
        print(alist)
        i+=1
    elif stack[-1]==-1 and j==0:
        anw=False
        break

    elif stack[-1]==goal:
        stack.pop()
        print(stack)
        alist.append('-')
        print(alist)
        j+=1

if anw==False:
    print('NO')
else:
    for i in alist:
        print(i)



