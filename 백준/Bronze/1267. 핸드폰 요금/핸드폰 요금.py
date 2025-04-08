def main() -> None:
    from sys import stdin
    from collections import deque, defaultdict
    from heapq import heappush, heappop
    from math import ceil, log2
    f = stdin.readline

    N = int(f())
    l = list(map(int, f().split()))

    a, b = 0, 0
    for e in l:
        a += ceil((e+1)/30)*10
        b += ceil((e+1)/60)*15
    if a < b:
        print('Y', a)
    elif a > b:
        print('M', b)
    else:
        print('Y M', a)

main()