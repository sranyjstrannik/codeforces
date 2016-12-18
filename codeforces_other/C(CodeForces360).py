s=input().split()
n,m=int(s[0]),int(s[1]) #количество вершин и рёбер соответственно

A,B=[],[]
ribs = []

for i in range(0,m):
        s = input().split()
        p1=int(s[0])
        p2=int(s[1])
        if (len(A)+len(B)==0):
                A+=[p1]
                B+=[p2]
                continue
        if ((p1 in A) and (p2 in A)) or ((p1 in B) and (p2 in B)):
                print(-1)
                quit()
        if (p1 in A) or (p2 in A):
                #всё начинается в т.A
                if p2 in A: p1,p2=p2,p1
                if p2 not in B: B+=[p2]
        elif (p1 in B) or (p2 in B):
                if p2 in B: p1,p2=p2,p1
                if p2 not in A: A+=[p2]
        else: #случай, когда вершин вообще нет в разбиении
               #как именно лучше добавить ребро?
               #сохраним это ребро на всякий случай на потом
                ribs+=[[p1,p2]]


#теперь мучаем оставшиеся рёбра
lastlen=0
while len(ribs)!=lastlen:
        lastlen=len(ribs)
        for rib in ribs:
                if ((rib[0] in A) and (rib[1] in A)) or ((rib[0] in B) and (rib[1] in B)):
                        print(-1)
                        quit()
                if (rib[0] in A) or (rib[1] in A) or (rib[0] in B) or (rib[1] in B):
                        #что-то делаем с ребром
                        if rib[0] in A:
                                if rib[1] not in B: B+=[rib[1]]
                        elif rib[1] in A:
                                if rib[0] not in B: B+=[rib[0]]
                        elif rib[0] in B:
                                if rib[1] not in A: A+=[rib[1]]
                        elif rib[1] in B:
                                if rib[0] not in A: A+=[rib[0]]
                        ribs.remove(rib)
                        break
        #добавляем наугад
        if ribs:
                rib = ribs[0]
                ribs.remove(rib)
                A+=[rib[0]]
                B+=[rib[1]]
        
if len(ribs):
        print(-1)
        quit()

                
#выводим результат
print(len(A))
s=''
for a in A: s+=str(a)+" "
print(s)

print(len(B))
s=''
for a in B: s+=str(a)+" "
print(s)
