import sys
from itertools import groupby

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def getMax(x, y):
  row = 0
  col = 0
  for k, g in groupby(board[x]):
    row = max(row, len(list(g)))
  for k, g in groupby(list(zip(*board))[y]):
    col = max(col, len(list(g)))
  return max(row, col)

ans = 0
for i in range(N):
  for j in range(N):
    ans = max(ans, getMax(i, j))

for i in range(N):
  for j in range(N):
    for r, c in zip(dx, dy):
      if -1 < i + r < N and -1 < j + c < N:
        if board[i][j] != board[i + r][j + c]:
          tmp = board[i][j]
          board[i][j] = board[i + r][j + c]
          board[i + r][j + c] = tmp

          ans = max(ans, getMax(i, j))

          board[i + r][j + c] = board[i][j]
          board[i][j] = tmp

print(ans)