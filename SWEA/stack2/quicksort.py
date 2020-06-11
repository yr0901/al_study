#퀵정렬 알고리즘
tlist=[69,10,30,2,16,8,31,22]

def quicksort(start, end, tlist):
    start=0
    end=len(tlist)-1
    pivot=(start+end)//2
    l=tlist[start]
    r=tlist[end]

    #partition
    L=tlist[start:]
    R=tlist[:end]
    while l<r:
        while tlist[start] <tlist[pivot] and l<r : start+=1
        while end>pivot and r>l:end-=1
        if l<r:
            if l==pivot:
                pivot=r
            tlist[l],tlist[r]=tlist[r],tlist[l]
            tlist[pivot], tlist[r] = tlist[r], tlist[pivot]
        quicksort(start, pivot-1, L)
        quicksort(pivot+1, end, R)

quicksort(0, len(tlist)-1, tlist)