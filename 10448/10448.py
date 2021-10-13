import sys

T = int(sys.stdin.readline())

f = lambda x: (x * (x + 1)) // 2

def solve():
  K = int(sys.stdin.readline())
  for i in range(1, 50):
    for j in range(1, 50):
      for k in range(1, 50):
        if f(i) + f(j) + f(k) == K:
          return 1
  return 0

for _ in range(T):
  print(solve())