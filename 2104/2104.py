import sys
sys.setrecursionlimit(10 ** 7)

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
pSum = [0] * (N + 1)

# calc prefix sum
for i, v in enumerate(l):
  pSum[i+1] = pSum[i] + v

# using divide & conquer
def solve(i, j):
  # base case: arr size = 1
  if i == j:
    return l[i] ** 2

  # base case: arr size = 2
  if j - i == 1:
    return max(l[i] ** 2, l[j] ** 2, (l[i] + l[j]) * min(l[i], l[j]))

  mid = (j + i) // 2

  # divide left and right
  left = solve(i, mid)
  right = solve(mid, j)
  s = e = mid
  m = l[mid]
  res = m * m

  # calc when the answer is both sides
  while(e - s < j - i):
    p = l[s-1] if s > i else l[s]
    q = l[e+1] if e < j else l[e]
    if s == i:
      m = min(m, q)
      e += 1
    elif e == j:
      m = min(m, p)
      s -= 1
    else:
      if p <= q:
        m = min(m, q)
        e += 1
      else:
        m = min(m, p)
        s -= 1
    res = max(res, (pSum[e+1] - pSum[s]) * m)
  
  return max(left, right, res)

print(solve(0, N-1))