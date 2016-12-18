def main(n):
    _32n = 3 * n / 2
    _32n_ = int(_32n) + bool(_32n % 1)
    for z in range(2, min(int(_32n)+bool(_32n%1), 10000)):
        for y in range(z+1,10000):
            try:
                x_ = -n*z*y/(n*(z+y) - 2*z*y)
            except: continue
            if not x_%1 and 10001 > x_ >1:
                return "{} {} {}".format(int(x_), y, z)
    return "-1"

n = int(input())
print(main(n))