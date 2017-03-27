import math

n = int(input())
a = list(map(int, input().split()))
m = min(a)

for cnt in range(m+1, 1, -1):
    count = 0
    flag = True
    for b in a:
        if (b % cnt) in [cnt-1, 0]:
            count += math.ceil(b / cnt)
        else:
            flag = False
            break
    if flag:
        print(count)
        exit()

