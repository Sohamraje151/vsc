print("\n24.Write a python program to count the elements in a list until an element is a tuple.\n ans=")
l=[1,2,3,'hi',('demo',32),(45.76,2,'hi'),'bye',44]
n=0
for i in l:
    if isinstance(i, tuple):
        break
    n+=1
print(n) 

