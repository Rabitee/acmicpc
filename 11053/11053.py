import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

print(max(dp))