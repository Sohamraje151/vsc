print("\n5.Write a python program to add an item in a tuple.\n ans=")
a=12,'demo',20.21,'hello'
print(a)
alist=list(a)#converting a tuple into a list then add values in it and then again convert it into a tuple.
alist.append('something')
alist.append(4.42)
a=tuple(alist)
print(a)
a=a+(87,)#using merge of tuples with + operator you can add an element and it will create a new tuple.
a=a[:4]+(3,2,1)+a[4:-1]#adding items in a specific index .
print(a)