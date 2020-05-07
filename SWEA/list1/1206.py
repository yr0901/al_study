import sys

sys.stdin = open('1206input.txt', 'r')
to = 10

for n in range(to):

    testcase = int(input())
    testlist= list(map(int, input().split(' ')))
    count=0

    for i in range(2,len(testlist)-2):
        templist = []
        if testlist[i]<=testlist[i+1] or testlist[i]<=testlist[i+2]:
            continue
        elif testlist[i]<=testlist[i-1] or testlist[i]<=testlist[i-2]:
            continue

        templist=[testlist[i-2],testlist[i-1],testlist[i+2],testlist[i+1]]
        count+=testlist[i]-max(templist)


    print('#{} {}'.format(n+1,count))