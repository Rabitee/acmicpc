import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1]*N
left = 0
right = N-1
f = lambda x,y: (x+y) // 2
mid = f(left, right)
while True:
    
    break
print(max(dp))