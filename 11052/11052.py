import sys

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [e for e in p]

for i in range(1, N):
    for j in range(i):
        dp[i] = max(dp[i], dp[j] + dp[i-j-1])

print(max(dp))