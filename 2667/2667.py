import sys

N = int(sys.stdin.readline())
m = []
m.append([0]*(N+2))
for _ in range(N):
    m.append(list(map(int, sys.stdin.readline().rstrip().ljust(N+1, '0').rjust(N+2, '0'))))
m.append([0]*(N+2))

q = []
sizelist = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def serach():
    size = 1
    while q:
        x,y = q.pop(0)
        for i in range(4):
            if m[x+dx[i]][y+dy[i]] == 1:
                m[x+dx[i]][y+dy[i]] = 0
                q.append((x+dx[i], y+dy[i]))
                size += 1
    sizelist.append(size)

for i in range(1,N+1):
    for j in range(1,N+1):
        if m[i][j] == 1:
            m[i][j] = 0
            q.append((i, j))
            serach()

print(len(sizelist))
sizelist.sort()
for i in range(len(sizelist)):
    print(sizelist[i])