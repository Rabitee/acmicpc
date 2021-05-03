import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
pair = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [[0, 0] for _ in range(K)]

for i in range(N):
  w, v = pair[i]
  # reverse iterator: to avoid considering current input twice
  for j in range(K-1, w-2, -1):
    if dp[j][0] + w <= j + 1:
      dp[j][0] += w
      dp[j][1] += v
    elif dp[j-w][0] + w <= j + 1:
      if dp[j][1] < dp[j-w][1] + v:
        dp[j][0] = dp[j-w][0] + w
        dp[j][1] = dp[j-w][1] + v
    elif dp[j][1] < v:
      dp[j] = pair[i]
print(max(dp, key=lambda x: x[1])[1])