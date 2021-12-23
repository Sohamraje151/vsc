import os
f=open("demo.txt","w+")
f.write("First line is write and read\nSecond line is here\nNext line\nAnother line")
f.seek(0)
print(f.read())
f.close()
os.rename("demo.txt", "sample.txt")
