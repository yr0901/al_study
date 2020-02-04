nlen=int(input())
nlist=list(map(int, input().split()))
temp=[]

for i in range(nlen-1):
    temp.append(nlist[i]-nlist[i+1])

lenlist=[]
if nlen==1:
    print(1)
else:
    while sum(lenlist)<=len(nlist):
        i=0
        if temp[i]<=0:
            for n in range(len(temp)):
                if temp[n]>0:
                    temp=temp[i:]
                    lenlist.append(i)
                    break
                else:
                    i+=1
                    lenlist.append(i)

        elif temp[i]>=0:
            for n in range(len(temp)):
                if temp[n]<0:
                    temp=temp[i:]
                    lenlist.append(i)
                    break
                else:
                    i+=1
                    lenlist.append(i)
    print(max(lenlist)+1)







