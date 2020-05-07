<<<<<<< HEAD
tc = int(input())

def car():
    k, n, m = map(int, input().split())
    stops = list(map(int, input().split()))
    charge = k
    count = 0
    j = 0
=======
def car(num, caselist):   
    templist=[0]
    for i in range(num[2]):
        if templist[-1]>num[1]:
            break
        templist.append(templist[i]+num[0])
    a=0
    while True:
        if templist[a]>caselist[a]:
            templist = templist[:a]
            templist.append(caselist[a])
            while len(templist)==len(caselist):
                templist.append(templist[-1]+num[0])
            a=0
            continue

        if templist[a] > num[1]:
            return len(templist)
        a+=1
        
test = int(input())
list1=[]
>>>>>>> 10451a913ef1d08f17b78a41f8f2a5da38f22e8a

    for i in range(len(stops) - 1):
        if stops[i+1] - stops[i] > k:
            count = 0
            break

    else:
        while j < len(stops)-1:
            if charge >= stops[j] and charge < stops[j+1]:
                charge = stops[j]
                count += 1
                j += 1
                charge += k
            else:
                j += 1
        if stops[-1] <= charge < n:
            charge = stops[-1]
            count += 1

    print("#{} {}".format(t+1, count))

for t in range(tc):
    car()