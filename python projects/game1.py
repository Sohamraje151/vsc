#game1-snake water gun game
import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
print("\n************Welcome to my new game************\n")
print("Computers term\n")
randNo=random.randint(1, 3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
print("Your term")
you=input("select (s) for snake,(w) for water and (g) for gun: ")
print(f"Computer chose {comp}")
print(f"You chose {you}")
a=gamewin(comp,you)
if a==None:
    print("the game is tie...!")
elif a==True:
    print("You are win...!")
else:
    print("you are lose...!")
