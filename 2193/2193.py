# https://www.acmicpc.net/problem/2193

import sys

N = int(sys.stdin.readline())

dp = [1, 1]

for i in range(2, N):
    dp.append(sum(dp[:i-1]) + 1)

print(dp[N-1])