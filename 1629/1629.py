import sys
sys.setrecursionlimit(10 ** 7)

A, B, C = map(int, sys.stdin.readline().split())

def f(x, y):
  return (x ** y) % C

def solve(x, y):
  if y <= 2:
    return f(x, y)
  res = f(solve(x, y // 2), 2)
  if y % 2 == 1:
    res = (res * x) % C
  return res

print(solve(A, B))