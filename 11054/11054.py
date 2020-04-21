import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().rstrip().split()))
rl = list(reversed(l))
inc = [1]*N
desc = [1]*N
bitonic = [0]*N

for i in range(1, N):
    for j in range(i):
        if l[i] > l[j] and inc[i] <= inc[j]:
            inc[i] = inc[j] + 1
        if rl[i] > rl[j] and desc[i] <= desc[j]:
            desc[i] = desc[j] + 1
for i in range(N):
    bitonic[i] = inc[i] + desc[(N - 1) - i] - 1

print(max(bitonic))