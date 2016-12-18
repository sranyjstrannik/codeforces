n = int(input())
M,C = 0,0
for i in range(0,n):
    game = input().split()
    if int(game[0])>int(game[1]):
        M+=1
    elif int(game[1])>int(game[0]):
        C+=1
    
if M>C: print("Mishka")
elif C>M: print("Chris")
else: print("Friendship is magic!^^")

