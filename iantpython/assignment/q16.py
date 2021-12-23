print("\n16.Write a python program to convert a tuple into a dictionary.\n ans=")
t2=('india','US','UK')
t1=(1,2,3)
print(t1)
print(t2)
if len(t1)==len(t2):
    d=dict(zip(t1,t2))
print("Dictionary converted from tuple:",d)
