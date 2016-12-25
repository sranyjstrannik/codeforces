n = int(input())
way = input()

def f(way):
    if len(way) == 1:
        return 1
    if len(way) == 0:
        return 0
    current = way[0]
    next = way[1]
    way = way[2:]
    while current == next:
        if len(way):
            current = next
            next = way[0]
            way = way[1:]
        else: return 1
    # дошли до поворота
    total = 0
    if ((current == 'R' and next == 'L') or
            (current == 'L' and next == 'R')): total += 1
    # идем до конца
    current = next
    next = way[0]
    way = way[1:]
    while current == next:
        if len(way):
            current = next
            next = way[0]
            way = way[1:]
        else: return 1+total
    # дошли до поворота
    if ((current == 'R' and next == 'L') or
            (current == 'L' and next == 'R')): return 1+total+f(way)
    return total+f(way[1:])

print(f(way))