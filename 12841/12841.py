import sys

n = int(sys.stdin.readline())
crosswalk = list(map(int, sys.stdin.readline().split()))
leftroad = [0] + list(map(int, sys.stdin.readline().split()))
rightroad = [0] + list(map(int, sys.stdin.readline().split()))

d = leftroad[0] + crosswalk[0] - rightroad[0]
l = 0
r = 0
idx = 0
for i, v in enumerate(crosswalk):
  l += leftroad[i]
  r += rightroad[i]
  tmp = l + v - r
  if tmp < d:
    idx = i + 1
    d = tmp

print(idx, sum(rightroad) + d)