import sys, re

def input():
    return sys.stdin.readline()

t = input()
lent = len(t)
p = input()[:-1]
t_with_flags = [True] * lent
p_with_flags =[[m.start(0) for m in re.finditer(s, t)] for s in p]


step = 0
for next_ in map(int, input().split()):
    t_with_flags[next_-1] = False
    smallest = -1
    for indexes in p_with_flags:
        flag = False
        # ищем такой индекс, что он еще не удален
        # и наименьший
        for i in indexes:
            if i > smallest:
                if t_with_flags[i]:
                    flag = True
                    smallest = i
                    break
        if not flag:
            sys.stdout.write(str(step))
            sys.exit(0)
    step += 1
sys.stdout.write(str(step))