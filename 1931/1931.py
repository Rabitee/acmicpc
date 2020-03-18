import sys

N = int(sys.stdin.readline())
l = []

for _ in range(N):
    (k, v) = map(int, sys.stdin.readline().rstrip().split())
    l.append((k, v))

l = sorted(l, key=lambda x:(x[1], x[0]))
last = l[0][1]
cnt = 1

if l[0][0] == l[0][1]:
    cnt = 0

for e in l:
    if last <= e[0]:
        last = e[1]
        cnt += 1
        
print(cnt)