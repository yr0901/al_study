testnum=int(input())

list1=[]
for test in range(testnum):
    num=int(input())
    caselist=list(input())
    templist=[]

    for i in caselist:
        templist.append(caselist.count(i))
    max_num=max(templist)
    if max_num==1:
        num_index = caselist.index(max(caselist))
    else:
        num_index = templist.index(max_num)
    strr = f'#{test+1} {caselist[num_index]} {templist[num_index]}'
    list1.append(strr)

for i in list1:
    print(i)