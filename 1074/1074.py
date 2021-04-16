import sys

N, r, c = map(int, sys.stdin.readline().rstrip().split())

def solve(n, row, col):
  if n == 2:
    return ((r - row) * 2) + (c - col) + 1
  
  nMid = n // 2
  rMid = ((2 * row) + n) // 2
  cMid = ((2 * col) + n) // 2

  if r < rMid:
    if c < cMid:
      return solve(nMid, row, col)
    else:
      return (nMid ** 2) + solve(nMid, row, cMid)
  else:
    if c < cMid:
      return ((nMid ** 2) * 2) + solve(nMid, rMid, col)
    else:
      return ((nMid ** 2) * 3) + solve(nMid, rMid, cMid)

print(solve(2 ** N, 0, 0) - 1)