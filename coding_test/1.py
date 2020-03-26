import sys

N = int(sys.stdin.readline())
part_times = []
for _ in range(N):
    part_times.append(list(map(int, sys.stdin.readline().rstrip().split())))

def solution(part_times):
    part_times = sorted(part_times, key=lambda x:(x[1], x[0], x[2]))
    dp = [t[2] for t in part_times]
    q = [t[:2] for t in part_times]

    for i in range(1, len(q)):
        for j in range(0, i):
            if q[j][1] <= part_times[i][0]:
                dp[i] = max(dp[i], dp[j] + part_times[i][2])

    return max(dp)
print(solution(part_times))