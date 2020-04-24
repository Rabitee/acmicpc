import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
l = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
d = [[0]*n for _ in range(n)]
p = [[0]*n for _ in range(n)]

for i in range(m):
    start = l[i][0] - 1
    end = l[i][1] - 1
    price = l[i][2]
    if d[start][end] == 0:
        d[start][end] = price
    else:
        d[start][end] = min(d[start][end], price)
    p[start][end] = start

for i in range(n):
    for j in range(n):
        for k in range(n):
            if (d[k][j] == 0 or d[k][j] > d[k][i] + d[i][j]) and d[k][i] > 0 and d[i][j] > 0 and k != j:
                d[k][j] = d[k][i] + d[i][j]
                p[k][j] = i

for i in range(n):
    print(*d[i])