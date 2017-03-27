import sys, re

def input():
    return sys.stdin.readline()

t = input() # слово, из которого всё удаляется
lent = len(t)
p = input() # слово, вхождения которого проверяем
p_with_flags =[[m.start(0) for m in re.finditer(s, t)] for s in p]

need_delete = list(map(int, input().split()))

left = 0
right = len(need_delete)+1
while left < right:
    middle = (left + right + 1) // 2
    if middle == right: break
    checks = [True] * lent
    for i in need_delete[:middle]:
        checks[i-1] = False
    smallest = -1
    another_flag = True # всё хорошо
    for indexes in p_with_flags: # проверяеяем для всех букв
        flag = False # не нашли для данной буквы подходящих вхождений
        for i in indexes:
            if i > smallest:
                if checks[i]:
                    smallest = i
                    flag = True # нашли подходящее вхождение
                    break
        if not flag:
            right = middle
            another_flag = False
            break
    if another_flag:
        left = middle

sys.stdout.write(str(left))