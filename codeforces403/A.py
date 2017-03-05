import sys

def input():
    return sys.stdin.readline()

n = int(input())
nums = list(map(int, input().split()))
flags = [0]*100000
max_ = 0
current = 0
for num in nums:
    current += 1
    if flags[num] == 1:
        current -= 2
        max_ = max(max_, current+1)
    else:
        flags[num] = 1
print(max_)