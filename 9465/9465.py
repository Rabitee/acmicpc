import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    l = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    for i in range(n):
        dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) + l[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2], dp[1][i-2]) + l[1][i]
    print(max(dp[0][n-1], dp[1][n-1]))