import sys
sys.setrecursionlimit(100000)

M, N = map(int, sys.stdin.readline().rstrip().split())
m = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(M):
    m.append(list(map(int, sys.stdin.readline().rstrip().split())))
dp = [[0 for _ in range(N)] for _ in range(M)]
dp[0][0] = 1
visited = set()

def check(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    return True

def f(x, y):
    if x == 0 and y == 0:
        return
    for i in range(4):
        if check(x+dx[i], y+dy[i]) and m[y][x] < m[y+dy[i]][x+dx[i]]:
            if (x+dx[i], y+dy[i], x, y) in visited:
                pass
            else:
                f(x+dx[i], y+dy[i])
                if (x+dx[i], y+dy[i], x, y) not in visited:
                    dp[y][x] += dp[y+dy[i]][x+dx[i]]
                    visited.add((x+dx[i], y+dy[i], x, y))
f(N-1, M-1)
print(dp[M-1][N-1])