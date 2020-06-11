#연산
from collections import deque

def BFS(start, end):
    deq = deque()


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    BFS(N, M)