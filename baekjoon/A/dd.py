T = int(input())
t = 0
while t < T:
    t += 1
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stop_No = [int(input()) for _ in range(P)]
    what_times = [0]*P
    i = 0

    while i < N:
        for j in range(line[i][0]-1, line[i][1]):
            what_times[j] += 1
        i += 1
    print('#'+str(t)+' ', end='')
    print(*what_times)
