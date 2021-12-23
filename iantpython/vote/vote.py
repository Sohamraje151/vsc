print("\n********welcome********\n")

a=0

while a==0:
    b=input("Enter (Y) or (y) for start...!!!\notherwise enter (Q) or (q) for exit...!!!\nEnter: ")
    if b=='Y' or b=='y':
        age=int(input("Enter your age:"))
        print("calculating....")
        if age<=0:
            print("Something went wrong....!!!! :( :( :( :(\nplease enter valid number...!!!\n")
        elif age<18 or age>50:
         print("You are not eligible for voting ....!!!\n")
        else:
         print("You are eligible for voting\n")
    elif b=='q' or b=='Q':
        break
    
