import sys

n,k = map(int, sys.stdin.readline().rstrip().split())
v = []
for _ in range(n):
    v.append(int(sys.stdin.readline()))
dp = [0]*(k+1)
v.sort()

for e in v:
    for i in range(e, k+1):
        if e == 1 or i == e:
            dp[i] += 1
        else:
            dp[i] += dp[i-e]

print(dp[k])