#Snake Water Gun Game 

import random

def gamewin(comp , you):

# condition based on game rule     
    if(comp == you):
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
            
print("com turn : snake(s) water(w) gun(g)?")


computer_choose = random.randint(1 , 3)
if computer_choose == 1:
    comp = 's'
elif computer_choose == 2:
    comp = 'w'
elif computer_choose == 3:
    comp = 'g'
    
you = input("your turn : snake(s) water(w) gun(g)?")

a = gamewin(comp , you)

print(f"computer choose {comp}")
print(f"you choose {you}")

#announce winner
if a == None:
    print("the game is tie!")
elif a:
    print("you win!")
else:
    print("you lose!")

