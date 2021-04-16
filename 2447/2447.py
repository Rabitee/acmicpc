import sys
sys.setrecursionlimit(10 ** 7)

N = int(sys.stdin.readline())
grid = [[' ' for _ in range(N)] for _ in range(N)]

def star(x, y):
  for i in range(3):
    for j in range(3):
      if i == 1 and j == 1:
        pass
      else:
        grid[x + i][y + j] = '*'

def solve(n, r, c):
  if n == 3:
    star(r, c)
    return
  
  nTri = n // 3

  for i in range(3):
    for j in range(3):
      if i == 1 and j == 1:
        pass
      else:
        solve(nTri, r + (nTri * i), c + (nTri * j))

solve(N, 0, 0)
for i in range(N):
  print(''.join(grid[i]))