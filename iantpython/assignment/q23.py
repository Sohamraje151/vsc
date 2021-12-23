print("\n23.Write a python program to sort tuple by its float element.\n ans=")
sdata=[('item1',12.20),('item2',15.10),('item3',24.5)]
print(sorted(sdata, key=lambda x: float(x[1]),reverse=True))