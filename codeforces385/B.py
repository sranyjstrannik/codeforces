import numpy as np

n,m = map(int,input().split())
A = [['X' for j in range(m)] for i in range(n)]
for i in range(n):
    A[i] = list(input())

A = np.array([b for b in A if 'X' in b]).T
A = np.array([b for b in A if 'X' in b])
if '.' in A:
    print("NO")
else: print("YES")
