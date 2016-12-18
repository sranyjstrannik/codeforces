n,k = input().split()
n,k = int(n),int(k)

c = [int(t) for t in input().split()]
k = [int(t) for t in input().split()]

total = 0
for ci in range(len(c)-1):
    total+=c[ci]*c[ci+1]

total+=c[-1]*c[0]

for ki in range(len(k)):
    for i in range(len(c)):
        if abs(i-ki)>1 and (ki!=(len(c)-1) and i!=0):
            total+=c[i]*c[ki]
            print(i)
            print(ki)

for k1 in range(len(k)):
    for k2 in range(k1,len(k)):
        if k1!=k2: total-=c[k1]*c[k2]

print(total)
