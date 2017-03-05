import sys, copy
from collections import Counter

def input():
    return sys.stdin.readline()


def two_variants(name1, name2):
    return name1[:3], name1[:2]+name2[0]


N = int(input())
names = [two_variants(*input().split(' ')) for _ in range(N)]
first_names = [fn[0] for fn in names]
first_names_set = set(first_names)
first_names_count = Counter(first_names)
second_names = [sn[1] for sn in names]
second_names_set = set(second_names)
result = []

for i in range(N):
    name = first_names[i]
    if first_names_count[name] > 1 or name in result:
        name = second_names[i]
    if name in result:
        print('NO')
        sys.exit(0)
    result.append(name)

if len(result) != len(set(result)):
    print('NO')
    sys.exit(0)

print('YES')
print(*result, sep='\n')
