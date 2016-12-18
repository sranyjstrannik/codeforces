import math
s, x1, x2 = map(int, input().split())
t1, t2 = map(int, input().split())
p, d = map(int, input().split())

if x1 < x2 and d < 0:
    p = -p
    d = 1
elif x1 > x2 and d > 0:
    p = 2*s - p
    d = -1

if x1 > x2:
    p = s - p
    x1 = s - x1
    x2 = s - x2

if p > x1: #and 1/t1 > 1/t2:
    T = ((s - p) + s + x1)/(1/t1 - 1/t2)
else:
    T = (x1 - p)/(1/t1 - 1/t2)

if T >= 0:
    X = x1 + T*(1/t2)
    if X > x2:
        print(round(math.ceil((x2-x1)*t2)))
    else:
        print(round(math.ceil(min((x2-x1)*t2, (X-x1)*t2 + (x2-X)*t1))))
else:
    print((x2-x1)*t2)