#의석이의 세로로 말해요

tcase = int(input())

for tc in range(tcase):
    temp=[]
    arr=[[ '*' for _ in range(15)] for _ in range(5)]

    for i in range(5):
        st=input()
        for k in range(len(st)):
            arr[i][k] = st[k]
    anwlist=[]
    for n in range(15):
        for i in range(len(arr)):
            anwlist.append(arr[i][n])

    anw = ''.join(anwlist)
    anw=anw.replace('*', '')
    print('#{} {}'.format(tc+1,anw))