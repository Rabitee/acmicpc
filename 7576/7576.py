# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

M, N = map(int, input().split())

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
t = deque()
day = 0

for x in range(N):
    for y in range(M):
        if grid[x][y] == 1:
            q.append((x, y))
        elif grid[x][y] == 0:
            t.append((x, y))

def daypass():
    nextq = deque()
    while q:
        x, y = q.popleft()
        for i in range(4):
            if -1 < x+dx[i] < N:
                if -1 < y+dy[i] < M:
                    if grid[x+dx[i]][y+dy[i]] == 0:
                        grid[x+dx[i]][y+dy[i]] = 1
                        nextq.append((x+dx[i], y+dy[i]))
                        t.popleft()
    return nextq

while True:
    q = daypass()
    if q:
        day += 1
    else:
        if t:
            day = -1
        break

print(day)