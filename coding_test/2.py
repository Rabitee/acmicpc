import sys

N, total_sp = map(int, sys.stdin.readline().rstrip().split())
skills = []
for _ in range(N - 1):
    skills.append(list(map(int, sys.stdin.readline().rstrip().split())))

def solution(total_sp, skills):
    
print(solution(total_sp, skills))