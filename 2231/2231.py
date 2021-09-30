import sys

N = int(sys.stdin.readline())

def solve():
  for i in range(1, N+1):
    ans = i + sum(list(map(int, str(i))))
    if ans == N:
      return i
  return 0

print(solve())