import sys
sys.setrecursionlimit(10 ** 7)

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = [0]*3
x = [1, 0, 0]
y = [0, 1, 0]
z = [0, 0, 1]

def f(x):
  if x == -1:
    res[0] += 1
  elif x == 0:
    res[1] += 1
  else:
    res[2] += 1

def solve(n, row, col):
  if n == 1:
    f(paper[row][col])
    return
  
  flag = False
  for i in range(n):
    for j in range(n):
      if paper[row + i][col + j] != paper[row][col]:
        flag = True
        break
  
  if flag:
    p = n // 3
    for i in range(0, n, p):
      for j in range(0, n, p):
        solve(p, row + i, col + j)
  else:
    f(paper[row][col])

solve(N, 0, 0)
print(res[0])
print(res[1])
print(res[2])