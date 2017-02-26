import sys

def input():
    return sys.stdin.readline()

n, k = input().split()

deleted = 0
counted = 0
for s in n[::-1]:
    if s != '0':
        deleted += 1
    else:
        counted += 1
        if counted == int(k):
            print(deleted)
            sys.exit(0)
print(len(n) - 1)
