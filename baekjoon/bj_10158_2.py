#개미
w, h =map(int, input().split())
tempp, tempq =map(int, input().split())
t=int(input())
dx=1
dy=1

for i in range(1,t+1):
    if tempp==0 or tempp==w:
        dx*=-1
    elif tempq==0 or tempq==h:
        dy*=-1
    tempp+=dx
    tempq+=dy

print(tempp, tempq)