import sys

N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
impurities = []
crystal = []
e = [-1] * 4

for i in range(N):
  for j in range(N):
    if grid[i][j] == 1:
      impurities.append([i, j])
    elif grid[i][j] == 2:
      crystal.append([i, j])

def nSomething(l, rSize, cSize, r, c):
  cnt = 0
  for x, y in l:
    if r <= x < r + rSize and c <= y < c + cSize:
      cnt += 1
  return cnt

# rSize: row size, cSize: column size
# r: row position, c: column position
# x, y: impurity's position
# d: direction
# e: error(cutting is impossible)
def cut(rSize, cSize, r, c, x, y, d):
  # horizontal direction
  if d == 0:
    if nSomething(crystal, 1, cSize, x, c) == 0:
      p1 = [x - r, cSize, r, c]
      p2 = [rSize - (x - r) - 1, cSize, x + 1, c]
      return p1, p2
  # vertical direction
  else:
    if nSomething(crystal, rSize, 1, r, y) == 0:
      p1 = [rSize, y - c, r, c]
      p2 = [rSize, cSize - (y - c) - 1, r, y + 1]
      return p1, p2
  return e, e

# d == direction
def solve(rSize, cSize, r, c, d=-1):
  nCrystal = nSomething(crystal, rSize, cSize, r, c)
  nImpurity = nSomething(impurities, rSize, cSize, r, c)
  res = 0

  if nCrystal == 0:
    return 0
  elif nCrystal == 1:
    if nImpurity == 0:
      return 1
    else:
      return 0
  else:
    if nCrystal - nImpurity != 1:
      return 0
    
    for imp in impurities:
      x, y = imp
      if r <= x < rSize + r and c <= y < cSize + c:
        if d == -1:
          for i in range(2):
            p1, p2 = cut(rSize, cSize, r, c, x, y, i)
            a = 0 if p1 == e else solve(*p1, i ^ 1)
            b = 0 if p1 == e else solve(*p2, i ^ 1)
            res += a * b
        else:
          p1, p2 = cut(rSize, cSize, r, c, x, y, d)
          a = 0 if p1 == e else solve(*p1, d ^ 1)
          b = 0 if p1 == e else solve(*p2, d ^ 1)
          res += a * b
  return res

res = solve(N, N, 0, 0)
print(-1 if res == 0 else res)