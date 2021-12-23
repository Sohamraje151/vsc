def maximum(n1,n2,n3):
    print("Maximum number is:  ",end='\b')
    if n1>n2>n3:
        print(n1)
    elif n1>n3>n2:
        print(n1)
    elif n2>n1>n3:
        print(n2)
    elif n2>n3>n1:
        print(n2)
    elif n3>n2>n1:
        print(n3)
    else:
        print(n3)

a1=int(input("enter number1:"))
a2=int(input("enter number2:"))
a3=int(input("enter number3:"))
print("*********___using user defined function___**********")
maximum(a1,a2,a3)
print("*********___using inbuilt function___**********")
print("Maximum number is:",max(a1,a2,a3))
