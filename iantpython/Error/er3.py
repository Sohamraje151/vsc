try:
    def division():
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        print(f"Division of {a}/{b}=",a/b)
        if b==0:
            raise ArithmeticError
    division()
except ArithmeticError:
    print("You need to be cautious from now on")
