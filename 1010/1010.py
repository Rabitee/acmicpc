import sys

T = int(sys.stdin.readline())
f = [1]*31
def factor(x):
    if x == 0 or x == 1:
        return f[x]
    else:
        f[x] = x * factor(x-1)
        return f[x]
for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    print((factor(M)) // (factor(N) * factor(M-N)))