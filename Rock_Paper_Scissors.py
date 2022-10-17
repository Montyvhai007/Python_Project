import random
from time import sleep

print ("\n---------Rock Paper Scissors----------")
def rpcgame(a,b):
 # if the magnitudes r same it will be tie
 if a == b:         # a for computer b for player/you
    return None
 # if computer chose rock
 elif a == 'r':     # r for rock
    if b == 'p':    # p for paper
     return False
 elif b=='s':       # s for scissor
     return True
 # if the computer chose paper
 elif a == 'p':    
    if b == 'r':  
     return False
 elif b=='s':       
     return True
 # if the computer chose scissor
 elif a == 's':    
    if b == 'r':    
     return False
 elif b=='p':       
     return True
# now its computer turn to chose

print("\nComputers Turn")
n = random.randint(1,3)

if n==1:
    a = 'r'
elif n== 2:
    a= 'p'
elif n== 3:
    a= 's'
sleep(2)
print("Computer has chosen")
print ("\nNow its Your Turn")
sleep(1)
b = input("Type r for Rock p for Paper s for Scissor : ")

print(f"\nComputer chose  {a}")
print(f"You chose  {b}")

# time for result

result = rpcgame(a,b)
if result == None:
    sleep(1)
    print("Its a tie")
elif result :
    sleep(1)
    print("You Win")
else :
    sleep(1)
    print ("computer Wins")

print("------------------------------")

# fell free to merge on github

    