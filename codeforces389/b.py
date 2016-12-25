import sys

s = input()
t = input()

need_change = {}

for l1,l2 in zip(s,t):
    p = sorted([l1,l2])
    if p[0] in need_change:
        if need_change[p[0]] != p[1]:
            print(-1)
            sys.exit(0)
    elif p[0] != p[1]:
        need_change[p[0]] = p[1]

for k in need_change:
    if need_change[k] in need_change:
        print(-1)
        sys.exit(0)

print(len(need_change))
for key in need_change:
    print(key, need_change[key])