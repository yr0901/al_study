string = list(input())
stack=[]
isp={'(':0, '+':1,'-':1, '*':2, "/":2, ')':-1}
icp={'(':3, '+':1,'-':1, '*':2, "/":2, ')':-1}

for i in string:
    if i not in isp.keys():
        print(i, end='')
    else:
        if isp[i]==-1:
            while True:
                temp=stack.pop()
                if icp[temp]==3:
                    break
                print(temp, end='')

        elif len(stack)==0 or icp[i]>isp[stack[-1]]:
            stack.append(i)
        else:
            while len(stack)>0 and icp[i]<=isp[stack[-1]]:
                print(stack.pop(), end='')
            stack.append(i)

if stack:
    for i in range(len(stack)):
        print(stack.pop(), end='')