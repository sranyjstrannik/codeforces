n, k, g, b = map(int, input().split())

if g >= b:
    gs = 'G'
    bs = 'B'
else:
    g, b = b, g
    gs = 'B'
    bs = 'G'

if g-k*b>k:
    print("NO")
else:
    gblock = g//(b+1)
    i = g%(b+1)
    result = ''
    for j in range(b):
        result += gs*gblock
        if i > 0:
            i -= 1
            result += gs
        result += bs
    result += gs*gblock
    print(result)
