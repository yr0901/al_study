tcase=int(input())

for tc in range(tcase):
    string =input()
    temp=[[] for _ in range(4)]
    n=3
    err=0
    while n<=len(string):
        if string[n-3]=='S':
            s=string[n-2:n]
            if s not in temp[0]:
                temp[0].append(s)
            else:
                err+=1
            n+=3
        elif string[n-3]=='D':
            s=string[n-2:n]
            if s not in temp[1]:
                temp[1].append(s)
            else:
                err+=1
            n+=3
        elif string[n-3]=='H':
            s=string[n-2:n]
            if s not in temp[2]:
                temp[2].append(s)
            else:
                err+=1
            n+=3
        elif string[n-3]=='C':
            s=string[n-2:n]
            if s not in temp[3]:
                temp[3].append(s)
            else:
                err+=1
            n+=3
    if err==0:
        anw = [13-len(temp[i]) for i in range(4)]
        print('#{}'.format(tc+1), end=' ')
        print(*anw)
    else: 
        print('#{} ERROR'.format(tc+1))

