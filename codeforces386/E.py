from sys import exit
n,m = map(eval,input().split())
inp = map(eval,input().split())

doubles = {}
ch, nch = 0,0
for next in inp:
    if next in doubles: doubles[next] += 1
    else: doubles[next] = 0
    if next%2: nch += 1
    else: ch += 1

M = [0 for i in range(m)]

result = ''
# меняем четные на нечетные
if ch > nch:
    needed = (ch-nch)//2
    for next in inp:
        if not next%2 and doubles[next] > 0 and needed:
            needed -= 1
            # ищем подходящее число
            flag = False
            for j in range(m):
                if (j%2) and (j+1) not in doubles:
                    doubles[j+1] = 0
                    result += ' '+str(j+1)
                    flag = True
            if not flag:
                print("NO")
                exit(0)
        if needed == 0: break
    for next in inp:
        if not next%2 and needed: # меняем