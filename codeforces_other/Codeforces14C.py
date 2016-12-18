a = input()
if '.' not in a: a+='.'
while a[0]=='0': a=a[1::]
while a[-1]=='0': a=a[0:-1]

#cлучай отрицательной экспоненты
if a[0]==".":
        b=0
        while a[1]=='0':
                b-=1
                a='.'+a[2::]
        b-=1
        a=a[1]+'.'+a[2::].rstrip('0')
        if b!=0: s=a+"E"+str(b)
        else: s=a
        if '.E' in s: s=s.replace('.','')
        print(s)
        
#случай положительной экспоненты
else:
        b=a.index('.')-1
        a=a.replace('.','')
        while a[-1]=='0':
                a=a[0:-1]
                
        if b!=0:
                s=a[0]+'.'+a[1::]+"E"+str(b)
        else:
                s=a[0]+'.'+a[1::]

        if '.E' in s: s=s.replace('.','')
        print(s)


