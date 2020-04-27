import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
maze = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dp = [[0]*(M+2) for _ in range(N+2)]
dp[1][1] = maze[0][0]
for i in range(N):
    for j in range(M):
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j]) + maze[i][j]
print(dp[N][M])