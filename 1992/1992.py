import sys

N = int(sys.stdin.readline())

quadtree = [list(map(str, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

def solve(n, row, col):
  if n == 1:
    return quadtree[row][col]
  
  nMid = n // 2
  rMid = ((2 *row) + n) // 2
  cMid = ((2 *col) + n) // 2  

  flag = False
  for i in range(n):
    for j in range(n):
      if quadtree[row + i][col + j] != quadtree[row][col]:
        flag = True
        break
  if flag:
    lu = solve(nMid, row, col)
    ru = solve(nMid, row, cMid)
    ld = solve(nMid, rMid, col)
    rd = solve(nMid, rMid, cMid)
  else:
    return quadtree[row][col]

  return '(' + lu + ru + ld + rd + ')'

print(solve(N, 0, 0))