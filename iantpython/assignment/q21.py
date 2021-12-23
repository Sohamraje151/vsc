print("\n21.Write a python program to replace last value of tuples in a list.\n ans=")
slist=[(10,20,40),(40,50,60),(70,80,90)]
print("list before output:",slist)
slist[2]=list(slist[2])
slist[2][2]=100
slist[2]=tuple(slist[2])
print("After replacing:",slist)