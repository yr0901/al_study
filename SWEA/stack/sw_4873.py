#반복문자 지우기
import sys

sys.stdin = open('input.txt','r')

tcase= int(input())
for tc in range(tcase):
    string=input()
    stack=[]
    for alpha in string:
        if len(stack)==0 or alpha!=stack[-1]:
            stack.append(alpha)
        else:
            stack.pop()

    if len(stack)==1:
        anw=1
    else:
        anw=len(stack)
    print('#{} {}'.format(tc+1, anw))