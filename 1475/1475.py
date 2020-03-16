# https://www.acmicpc.net/problem/1475

import sys
import math

N = sys.stdin.readline().rstrip()
l = [0]*10

for e in N:
    l[int(e)] += 1

ll = l[:6]
ll.append(l[7])
ll.append(l[8])
m = math.ceil((l[6] + l[9]) / 2)
ll.append(m)
print(max(ll))