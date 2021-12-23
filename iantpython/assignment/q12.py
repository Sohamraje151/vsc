print("\n12.Write a python program to remove an item from a tuple.\n ans=")
h=('book',21,99.99,True,'hello',12)
print(h)
h=list(h)
h.remove('book')
h.remove(12)
h=tuple(h)
print(h)



