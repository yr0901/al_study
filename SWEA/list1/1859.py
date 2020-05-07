#백만장자 프로젝트

def backman(daynum, daylist):
    anw =0
    while True:
        max_num=max(daylist)
        max_index=daylist.index(max_num)

        if max_index ==0:
            answer=f'#{test+1} {anw}'
            return answer

        for i in range(0, max_index+1):
            anw +=max_num-daylist[i]

        if max_index ==len(daylist)-1:
            answer=f'#{test+1} {anw}'         
            return answer

        daylist = daylist[max_index+1:]


testcase = int(input())
list1=[]
for test in range(testcase):
    daynum=int(input())
    daylist = list(map(int, input().split()))
    list1.append(backman(daynum, daylist))

for i in list1:
    print(i)
