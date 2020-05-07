test = int(input())
list1=[]

for i in range(test):
    num=int(input())
    caselist=list(map(int, input().split()))
    list1.append(max(caselist)-min(caselist))

for i in list1:
    print(f'#{list1.index(i)+1} {i}')