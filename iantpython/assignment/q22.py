print("\n22.Write a python program to remove an empty tuple(s) from a list of tuples.\n ans=")
sample=[(),(),('',),('a','b'),('a','b','c'),('d')]
print(sample)
for i in sample:
    if i==(()):
        sample.remove(i)
        sample.remove(i)
print("Expected output:",sample)