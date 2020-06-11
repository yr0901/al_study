
'''
import sys
sys.stdin=open('input.txt','r')
'''
tcase = int(input())

for tc in range(tcase):
    tlist = list(input().split())
    stack=[]
    
    for i in tlist:
        if i.isdigit():
            stack.append(int(i))
        else:
            if len(stack)<2 and i!='.':
                anw='error'
                break
            elif i =='+':
                b=stack.pop()
                a=stack.pop()
                stack.append(a+b)
            elif i =='-':
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
            elif i =='*':
                b=stack.pop()
                a=stack.pop()
                stack.append(a*b)
            elif i =='/':
                b=stack.pop()
                a=stack.pop()
                stack.append(a/b)
            else:
                anw=int(stack.pop())
    if len(stack)!=0:
        anw='error'

    print('#{} {}'.format(tc+1, anw))