def Dictionary():
    n=int(input("Enter number of peoples:"))
    l1=[]
    l2=[]
    for i in range(n):
        a=input("Enter name:")
        b=input("Enter marks:")
        l1.append(a)
        l2.append(b)
    print(l1)
    print(l2)
    D1.update(dict(zip(l1,l2)))
    print(D1)
def sort():
    print("Dictionary sorted by names(keys):",sorted(D1))
def remove():   
    k=input("Enter key:")
    if D1.get(k):
        print("yes key is present in dictionary..!!!\n=",D1)
        s=input("If you want to remove it plz enter 'Y / y' if not then enter 'N / n':")
        if s=='y' or s=='Y':
            D1.pop(k)
            print(f"{k} is succesfully removed...!!!")
            print("Dictionary is changed=",D1)
        else:
            print("Dictionary not changed=",D1)
def Add():
    a=input("Enter 'Y / y' if you want to add new entry\nEnter 'N / n' for No\n:")
    if a=='Y' or a=="y":
        Dictionary()
        print("Final Dictionary is:",D1)
    else:
        print("Dictionary is Unchanged=",D1)
D1={}
Dictionary()
sort()
remove()
Add()
