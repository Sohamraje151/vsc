print("\n********* continue statement *********\n")
str="python"
print(str)
for i in str:
    if i=='h':#it will skip the output 'h' if value of 'i' becomes 'h'
        continue
    print(i)
print("\n********* break statement *********\n")
str="python"
print(str)
for i in str:
    if i=='h':#it will break the output if value of 'i' becomes 'h'
        break
    print(i)
