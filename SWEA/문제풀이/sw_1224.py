#계산기3
import sys
sys.stdin=open('input.txt','r')

for tc in range(10):
    N=int(input())
    string = list(input())
    stack=[]
    tlist=[]
    isp={'(':0, '+':1,'-':1, '*':2, "/":2, ')':-1}
    icp={'(':3, '+':1,'-':1, '*':2, "/":2, ')':-1}

    for i in string:
        if i not in isp.keys():
            tlist.append(i)
        else:
            if isp[i]==-1:
                while True:
                    temp=stack.pop()
                    if icp[temp]==3:
                        break
                    tlist.append(temp)

            elif len(stack)==0 or icp[i]>isp[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)>0 and icp[i]<=isp[stack[-1]]:
                    tlist.append(stack.pop())
                stack.append(i)
    if stack:
        for i in range(len(stack)):
            tlist.append(stack.pop())

    stack2=[]
    for i in tlist:
        if i.isdigit():
            stack2.append(int(i))
        else:
            if i =='+':
                b=stack2.pop()
                a=stack2.pop()
                stack2.append(a+b)
            elif i =='-':
                b=stack2.pop()
                a=stack2.pop()
                stack2.append(a-b)
            elif i =='*':
                b=stack2.pop()
                a=stack2.pop()
                stack2.append(a*b)
            elif i =='/':
                b=stack2.pop()
                a=stack2.pop()
                stack2.append(a/b)
            # else:
            #     anw=int(stack2.pop())
    anw=stack2.pop()

    print('#{} {}'.format(tc+1, anw))
        
