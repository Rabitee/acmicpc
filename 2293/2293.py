import sys

n,k = map(int, sys.stdin.readline().rstrip().split())
v = []
for _ in range(n):
    v.append(int(sys.stdin.readline()))
dp = [0]*(k+1)
dp[0] = 1
v.sort()

for e in v:
    for i in range(e, k+1):
        dp[i] += dp[i-e]

print(dp[k])