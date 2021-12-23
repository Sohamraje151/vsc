try:
    a=input("Enter number1:")
    b=input("Enter number2:")
    c=a*b
    print("Multiplication is:",c)
except TypeError:
    print("Please Enter valide input...!!!")
else:
    print("Success...!!!")
