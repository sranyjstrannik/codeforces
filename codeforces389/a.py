n,m,k = map(int,input().split())

r = int(k/(2*m)) + (1 if k%(2*m) else 0)
d_ = k-(r-1)*m*2
d = int(d_/2) + int(d_%2)
if d_%2: s = 'L'
else: s = 'R'

print(r,d,s)