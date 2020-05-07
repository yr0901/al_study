#괄호검사
tcase=int(input())
for tc in range(tcase):
    string = input()
    stack=[]
    anw=1
    info=[0]*128
    info[ord(')')] ='('
    info[ord(']')] ='['
    info[ord('}')] ='{'
    info[ord('>')] ='<'
    
    for now in range(len(string)):
        if string[now] =='(' or string[now] =='[' or string[now] =='{' or string[now] =='<':
            stack.append(string[now])

        elif string[now] ==')' or string[now] ==']' or string[now] =='}' or string[now] =='>':
            if len(stack)!=0 and info[ord(string[now])]== stack[-1]:
                stack.pop()
            else: 
                anw=0
                break

    if len(stack)!=0:
        anw=0

    print(f'#{tc+1} {anw}')