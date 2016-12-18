a = int(input())
b = int(input())
c = int(input())

for i in range(a,-1,-1):
    if 2*i <= b and 4*i <= c:
        print(7*i)
        break
