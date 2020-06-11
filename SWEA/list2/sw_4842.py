tc=int(input())

for tcase in range(tc):
    num=int(input())
    tmp = list(map(int, input().split()))
    tlist=[]
    for k in range(num):
        if k&1: #홀수일 때
            tlist.append(min(tmp))
            tmp.remove(min(tmp))
        else: #짝수일때
            tlist.append(max(tmp))
            tmp.remove(max(tmp))
        if len(tlist)==10:
            break

    # tlist=map(str,tlist)
    # strr=' '.join(tlist)
    # print(f'#{tcase+1} {strr}')

    print('#{}'.format(tcase+1), end=' ')
    print(*tlist)
