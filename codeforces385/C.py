n,m,k = map(int,input().split())
capitals = list(map(int,input().split()))
ways = [list(map(int,input().split())) for i in range(m)]
connections = {i:[] for i in range(1, n+1)}
for w in ways:
    connections[w[0]] += [w[1]]
    connections[w[1]] += [w[0]]
domens = [0]*(n+1)

index = 0
for c in capitals:
    q = [c]
    index = c
    passed = []
    while len(q):
        e = q.pop()
        passed += [e]
        domens[e] = index
        for link in connections[e]:
            if link not in passed:
                q += [link]

added = 0
best = 0
for c in capitals:
    existedV = domens.count(c)
    best = max(best,existedV)
    existedW = 0
    for ind,d in enumerate(domens):
        if d == c:
            existedW += len(connections[ind])
    existedW = existedW // 2
    added += existedV*(existedV-1)//2-existedW

existedV = domens[1:].count(0)
existedW = 0
for ind,d in enumerate(domens[1:]):
    if d == 0:
        existedW += len(connections[ind+1])
existedW = existedW // 2
old_n = best
new_n = best+existedV
added += new_n*(new_n-1)//2 - old_n*(old_n-1)//2 - existedW
print(added)
