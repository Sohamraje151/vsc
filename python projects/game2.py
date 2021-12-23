# game2-rock paper scissor game
import random
def game(c,you):
    if c==you:
        return None
    elif c=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
    elif c=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif c=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
print("**********welcome to my new game-rock paper scissor game **********")
print("computers term \n computer selected from (r)for rock,(p) for paper and (s) for scissor \n")
r=random.randint(1, 3)
if r==1:
    c='r'
elif r==2:
    c='p'
elif r==3:
    c='s'
print("now it's your term \n")
you=input("select (r)for rock,(p) for paper and (s) for scissor: ")
print(f"\nComputer select {c}")
print(f"You select {you} \n")
a=game(c,you)
if a==None:
    print("the game is tie ...!")
elif a==True:
    print("Congrats You are winner ...!")
else:
    print("You are lose ...!")

