import sys

def input():
    return sys.stdin.readline()

n = int(input())
colors = [0 for _ in range(n+1)]
children = [list() for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    children[a].append(b)
    children[b].append(a)

# находим какую-нибудь вершину с одним ребенком
# она гарантированно существует
start = 0
for i in range(1, n+1):
    if len(children[i]) == 1:
        start = i
        break

colors[start] = 1
colors[children[start][0]] = 2
node = children[start][0]
Q = [node]

while len(Q):
    nd = Q.pop()
    banned_colors = [colors[nd]]
    for c in children[nd]:
        if colors[c] != 0:
            banned_colors.append(colors[c])
    for c in children[nd]:
        if colors[c] == 0:
            t = 0
            for i in range(1, n+1):
                if i not in banned_colors:
                    t = i
                    break
            colors[c] = t
            banned_colors.append(t)
            Q.append(c)
print(max(colors))
print(*colors[1:], sep=' ')
