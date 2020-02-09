#딱지놀이

round=int(input())

def fight(a,b):
    for k in [4,3,2,1]:
        if a[1:].count(k)>b[1:].count(k):
            return 'A'
        elif a[1:].count(k)<b[1:].count(k):
            return 'B'
        else:
            continue
    return 'D'

for r in range(round):
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    print(fight(a,b))


    

