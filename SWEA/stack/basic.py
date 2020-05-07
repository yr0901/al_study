#선택 정렬 재귀
list1=[1,6,23,5,23,75,25,64,2]

def selection(n, list1):
    if n ==len(list1):
        return list1
    where = n
    minn=list1[n]
    for i in range(n+1, len(list1)):
        if list1[i]<minn:
            minn=list1[i]
            where=i

    list1[n], list1[where] = list1[where], list1[n]
    
    return selection(n+1, list1)

print(selection(0, list1))