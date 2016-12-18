def encrypt(s):
    if len(s)%2:
        l = s[0]
        s = s[1:]
        s = s[::2][::-1] + s[1::2]
        s = s[:len(s)//2]+l+s[len(s)//2:]
        return s
    return s[::2][::-1] + s[1::2]

input()
print(encrypt(input()))