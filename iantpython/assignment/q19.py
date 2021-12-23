print("\n19.Write a python program to convert a list of tuples into a dictionary.\n ans=")
alist=[(1,2,3,4),('a','b','c','d')]
print("Before:",alist)
if len(alist[0])==len(alist[1]):
    dic=dict(zip(alist[0],alist[1]))
print("converted a list of tuples into a dictionary:",dic)