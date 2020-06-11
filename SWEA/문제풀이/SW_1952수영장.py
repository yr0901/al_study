#수영장
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    day, month, three, year = map(int, input().split())
    plan = list(map(int, input().split()))

change = month//day
for tt in range(12):
    if plan[tt]>=change:
        plan[tt] = month
    elif plan[tt]: plan[tt] = day

for tt in range(12):
    if plan[tt] == month:
        count += 1
    else:
        count = 0

    if count ==3:
        

    