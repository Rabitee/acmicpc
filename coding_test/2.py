import sys

N, total_sp = map(int, sys.stdin.readline().rstrip().split())
skills = []
for _ in range(N - 1):
    skills.append(list(map(int, sys.stdin.readline().rstrip().split())))

def solution(total_sp, skills):
    tree = {i + 1:None for i in range(len(skills) + 1)}
    for skill in skills:
        if tree[skill[0]] == None:
            tree[skill[0]] = [skill[1]]
        else:
            tree[skill[0]].append(skill[1])
    sp = [0] * (len(skills) + 1)

    def root(skills):
        l = [-1] * (len(skills) + 1)
        for skill in skills:
            l[skill[1] - 1] = skill[0] - 1
        return l.index(-1) + 1

    def f(tree, sp, node):
        if tree[node] == None:
            sp[node - 1] = 1
        else:
            for e in tree[node]:
                f(tree, sp, e)
            sp[node - 1] = sum(sp[e - 1] for e in tree[node])
    
    r = root(skills)
    f(tree, sp, r)
    v = int(total_sp / sum(sp))
    sp = list(map(lambda x:x*v, sp))
    return sp
    
print(solution(total_sp, skills))