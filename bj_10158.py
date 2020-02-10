#개미
w, h =map(int, input().split())
p, q =map(int, input().split())
t=int(input())
tempp=p
tempq=q

def ant(tempp, tempq,t):
    global p,q
    dx=1
    dy=1
    for i in range(1,t+1):
        if tempp==0 or tempp==w:
            dx*=-1
        elif tempq==0 or tempq==h:
            dy*=-1
        tempp+=dx
        tempq+=dy

        if  tempp==p and tempq==q and dx==1 and dy==1: #반복찾기
            i=t%i
            break
    return tempp, tempq, i

resultp, resultq, i = ant(tempp, tempq,t)
if i!=t:
    resultp, resultq,i = ant(resultp, resultq,i)
    
print(resultp, resultq)
