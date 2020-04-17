import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
l = []
for _ in range(N):
    l.append(list(map(int, sys.stdin.readline().rstrip().split())))
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = l[0][0]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + l[i][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + l[0][i]
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + l[i][j]
K = int(sys.stdin.readline())

for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().rstrip().split())
    a = dp[x-1][y-1]
    b = dp[x-1][j-2] if j-2 >= 0 else 0
    c = dp[i-2][y-1] if i-2 >= 0 else 0
    d = dp[i-2][j-2] if j-2 >= 0 and i-2 >= 0 else 0
    print(a - b - c + d)