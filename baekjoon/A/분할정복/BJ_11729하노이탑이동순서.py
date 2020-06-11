#하노이탑 이동순서

def hanoi(n,a,b,c): 
    if n==1: 
        move.append([a,c]) 
    else: 
        hanoi(n-1,a,c,b) 
        move.append([a,c]) 
        hanoi(n-1,b,a,c) 

N = int(input()) 
move = []

hanoi(N,1,2,3)

print(len(move))

for t in move:
    print(t[0], end=' ')
    print(t[1])
