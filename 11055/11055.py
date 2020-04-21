import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [e for e in A]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j] + A[i]:
            dp[i] = dp[j] + A[i]

print(max(dp))