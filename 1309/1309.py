import sys

N = int(sys.stdin.readline())
a = 1
b = 1
c = 3
for i in range(1, N):
    a = b
    b = c
    c = 2*b + a
print(c % 9901)