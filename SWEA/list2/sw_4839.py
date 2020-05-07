tc=int(input())

def counting(n,P):
    l=1
    r=P
    num=0
    for i in range(P):
        c=int((l+r)/2)
        if n<c:
            r=c
            num+=1
            continue

        elif n>c:
            l=c
            num+=1
            continue

        else:
            return num

for tcase in range(tc):
    P,A,B = map(int, input().split())

    if counting(A,P) >counting(B,P):
        print(f'#{tcase+1} B')
    elif counting(A,P) <counting(B,P):
        print(f'#{tcase+1} A')
    else:
        print(f'#{tcase+1} 0')