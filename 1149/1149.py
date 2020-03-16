# https://www.acmicpc.net/problem/1149

import sys

N = int(sys.stdin.readline())
board = []
dp = []
for _ in range(N):
    price = sys.stdin.readline().split()
    board.append(list(map(int, price)))

dp = board
for i in range(1,N):
    dp[i] = [min(dp[i-1][x-1], dp[i-1][x-2]) + board[i][x] for x in range(3)]

print(min(dp[-1]))