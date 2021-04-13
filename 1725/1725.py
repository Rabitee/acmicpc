import sys
sys.setrecursionlimit(10 ** 7)

N = int(sys.stdin.readline())
s = [] # stack
res = 0

for i in range(N):
  v = int(sys.stdin.readline())
  if not s:
    s.append((i, v))
  else:
    # push case: top < current histogram height
    if s[-1][1] < v:
      s.append((i, v))
    else:
      # pop case: top >= current histogram height
      while(True):
        if not s or s[-1][1] < v:
          break
        _, e = s.pop()

        # area: pop height * top histogram position
        # if stack is empty, top = 0
        j = s[-1][0] + 1 if s else 0
        res = max(res, e * (i - j))
      s.append((i, v))

while(s):
  _, e = s.pop()
  i = s[-1][0] + 1 if s else 0
  res = max(res, e * (N - i))

print(res)