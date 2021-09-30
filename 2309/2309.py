import sys

l = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
l = sorted(l)

def solve():
  for i in range(9):
    for j in range(i+1, 9):
      s = list(filter(lambda x: x != l[i] and x != l[j], l))
      if sum(s) == 100:
        for e in s:
          print(e)
        return

solve()