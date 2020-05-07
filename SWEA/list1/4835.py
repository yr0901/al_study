def neighbor(num, caselist):
    list1=[]
      
    for a in range(num[0]-num[1]+1):
        sum=0 
        for k in range(num[1]):
            sum+=caselist[a+k]
        list1.append(sum)
    return max(list1)-min(list1)

test = int(input())
list2=[]
for i in range(test):
    num=list(map(int, input().split()))
    caselist=list(map(int, input().split()))
    list2.append(neighbor(num, caselist))

for i in range(len(list2)):
    print('#{} {}'.format(i+1, list2[i]))