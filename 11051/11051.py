import sys
sys.setrecursionlimit(10 ** 7)

n, k = map(int, sys.stdin.readline().split())
dp = [[-1 for _ in range(k)] for _ in range(n)]
mod = 10007

def solve(n, r):
  if n == r or n == 0 or r == 0:
    return 1
  if r == 1:
    return n
  if dp[n-1][r-1] == -1:
    dp[n-1][r-1] = ((solve(n-1, r-1) % mod) + (solve(n-1, r) % mod)) % mod
  return dp[n-1][r-1]

print(solve(n, k))