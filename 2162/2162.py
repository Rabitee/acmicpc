import sys

N = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
di = {}
di[0].append([lines[0]])

def ccw(x1, y1, x2, y2, x3, y3):
    tmp = x1*y2 + x2*y3 + x3*y1
    tmp -= (x2*y1 + x3*y2 + x1*y3)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0