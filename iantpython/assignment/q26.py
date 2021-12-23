print("\n26.Write a python program to calculate the product,multiplying and all the numbers of a given tuple.\n ans=")
def product(n):
    t=list(ot)
    s=1
    for i in t:
        s*=i
    return s

ot=(4,3,2,2,-1,18)
print("original:",ot)
print("Product - multiplying all the numbers of the tuple:",product(ot))
ot=(2,4,8,8,3,2,9)
print("original:",ot)
print("Product - multiplying all the numbers of the tuple:",product(ot))
