#Fibonacci series
term=int(input("Enter the terms for Fibonacci series: "))
a=0
b=1
count=0
if term<=0:
    print("Please enter valid integer")
elif term==1:
    print("Fibonacci series upto:",term,"is",a)
else:
    print("Fibonacci series:")
    while count<term:
        print(a,end=" ")
        c=a+b
        a=b
        b=c
        count+=1
