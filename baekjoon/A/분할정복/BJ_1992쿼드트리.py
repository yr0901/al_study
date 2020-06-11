#쿼드트리

def CHECK(starty, startx, N):
    global answer

    length = N//2
    temp=''
    
    for sy in range(0, N, length):
        for sx in range(0, N, length):
            stop = False
            default = arr[starty+sy][startx+sx]
            for dy in range(length):
                for dx in range(length):
                    nexty = starty + sy+ dy
                    nextx = startx + sx+ dx
                    if length != 1: 
                        if arr[nexty][nextx] != default:
                            answer += '('
                            CHECK(starty+sy, startx+sx, length)
                            answer += ')'
                            stop = True
                            break
                    else:
                        temp += default
                        #print(temp)
                if stop:
                    break

            if not stop and length !=1 :
                answer += default

    if temp == '1111':
        answer += '1'
    elif temp == '0000':
        answer += '0'
        #print('hi')
    else: 
        answer += temp

N = int(input())
arr = [list(input()) for _ in range(N)]
answer = '('
CHECK(0,0,N)
answer += ')'
if answer == '(1111)':
    answer = '1'
elif answer == '(0000)':
    answer = '0'

print(answer)
