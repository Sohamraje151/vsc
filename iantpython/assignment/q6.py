print("\n6.Write a python program to convert a tuple to a string.\n ans=")
def convertstr(tup):
    s=''
    for i in tup:
        s=s+i
    return s
a='w','e','l','c','o','m','e','-to-','pune'
s=convertstr(a)
print(s)
