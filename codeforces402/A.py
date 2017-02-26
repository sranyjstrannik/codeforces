import sys

def input():
    return sys.stdin.readline()

n = int(input())
class_A = sorted(list(map(int, input().split())))
class_B = sorted(list(map(int, input().split())))

counts = [0]*6

total = 0
for i in range(1, 6):
    counts[i] = class_A.count(i) + class_B.count(i)
    if counts[i] % 2:
        print(-1)
        sys.exit(0)
    counts[i] //= 2

for i in range(1, 6):
    total += abs(counts[i] - class_A.count(i))

print(total // 2)

