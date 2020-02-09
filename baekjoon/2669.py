#직사각형 네개의 합집합의 면적 구하기
'''
dot = []
x=[]
y=[]

    for i in range(x1,x2+1):
        for i in range(y1,y2+1):
            dot.append([i,k])

    i=0
    count=0
    while True:
        temp=[]
        for a in range(len(dot)):
            if dot[a][1]==i:
                temp.append(dot[a][0])
                count+=max(temp)-min(temp)
        i+=1

        if 

'''
x=[0]*10
ans=[x]*10
count=0

for i in range(4):

    x1,y1,x2,y2 =map(int, input().split(' '))

    for i in range(x1,x2+1):
        for a in range(y1,y2+1):
            if ans[a][i]!=1:
                ans[a][i]=1
                count+=1

    print(count)
    

