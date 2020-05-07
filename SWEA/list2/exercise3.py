alist = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]

def selctionsort(tmp):
    for n in range(len(tmp)):
        min = n
        for i in range(n+1,len(tmp)):
            if tmp[min]>tmp[i]:
                min=i
        tmp[min], tmp[n] = tmp[n], tmp[min]
    return tmp

tmp=[]
for li in alist:
    for i in range(5):
        tmp.append(li[i])

tmp=selctionsort(tmp)
temp=[5,4,3,2,1]
num=0
x=0
y=-1
d=0
for k in range(len(temp)):
    if num==len(tmp)-1: #맨마지막
        alist[x][y+1]=tmp[-1]
        break

    if d==0:
        for i in range(temp[k]):
            y+=1
            alist[x][y]= tmp[num+i]
        num+=temp[k]

        for i in range(temp[k+1]):
            x+=1
            alist[x][y]=tmp[num+i]

        num+=temp[k+1]
        d=(d+1)%2
        
    else:
        for i in range(temp[k]):
            y-=1
            alist[x][y]= tmp[num+i]
        num+=temp[k]

        for i in range(temp[k+1]):
            x-=1
            alist[x][y]=tmp[num+i]  
        num+=temp[k+1]
        d=(d+1)%2
        print(num)
    
for k in alist:
    print(k)
    
#승민오빠 코드

arr = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]

ans = [[0 for _ in range(5)] for _ in range(5)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visit = [[False for _ in range(5)] for _ in range(5)]


ans_x = ans_y = 0
dir = 0

for it in range(25):
    min = 987654321
    x = y = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < min:
                min = arr[i][j]
                x = i
                y = j
    # print(min)
    arr[x][y] = 987654321
    ans[ans_x][ans_y] = min
    visit[ans_x][ans_y] = True

    if ans_x + dx[dir] >= 5 or ans_x+dx[dir] < 0 or ans_y+dy[dir] >= 5 or ans_y+dy[dir] < 0:
        dir = (dir+1)%4
        ans_x = ans_x + dx[dir]
        ans_y = ans_y + dy[dir]
        continue

    if visit[ans_x + dx[dir]][ans_y+dy[dir]]:
        dir = (dir + 1) % 4
        ans_x = ans_x + dx[dir]
        ans_y = ans_y + dy[dir]
        continue

    ans_x = ans_x + dx[dir]
    ans_y = ans_y + dy[dir]

for row in ans:
    print(*row)
