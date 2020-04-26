#미로탐색
from collections import deque

def BFS(starty, startx, depth):


N, M = map(int, input().split())
arr = [list(map(int, input().split))) for _ in range(N)]

#1이 길 0이 벽

BFS(0,0,depth)