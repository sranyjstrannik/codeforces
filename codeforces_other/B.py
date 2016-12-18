import numpy 

def gen(n):
    t = []
    for i in range(1,n+1):
        tj = [k for k in range(1,n+1)]
        if i>1: tj[i-1]=i+1
        t+=[tj]
    return numpy.matrix(t)

print(numpy.linalg.det(gen(255)))


