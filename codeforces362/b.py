s = input().split('e')
a = s[0].split('.')[0]
d = s[0].split('.')[1]
b = int(s[1])

if b<len(d):
    #случай, когда не надо нулей
    s=a + d[0:b]+'.'+d[b:]
    while s[-1] in ['.','0']:
        s=s[0:-1]
    while s[0] == "0":
        s=s[1:]
    if s[0]=='.': s="0"+s
    print(s)
else:
    s=a+d+"0"*(b-len(d))
    while s[0]=="0":
        s=s[1:]
    print(s)
