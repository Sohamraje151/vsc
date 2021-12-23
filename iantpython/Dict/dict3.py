n=int(input("Enter Number:"))
li1=[]
li2=[]
d={}
for i in range(1,n+1):
    li1.append(i)
    li2.append(i*i)
    d.update(dict(zip(li1,li2)))
print(li1)
print(li2)
print(d)

