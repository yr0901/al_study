#이진법
def Bit(N, num):
    output="0"
    n=0
    while 2**n <num:
        n+=1

    for i in range(n-1,-1,-1):
        if num&(1<<i) :
            output += '1'
        else:
            output += '0'
    return output

T = int(input())
for tc in range(T):
    N, num = input().split()

    #16 to 10
    num = int(num, 16)
    print(f'#{tc+2} {Bit(int(N),num)}')