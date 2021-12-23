try:
    s=[]
    n=int(input("enter number of list items:"))
    for i in range(n):    
        a=input("Enter a word:")
        if a=="anger":
            raise ValueError
        s.append(a)
    print(s)
except ValueError:
    print("Do not enter anger keyword\nuse another keyword.")
else :
    print("good")

