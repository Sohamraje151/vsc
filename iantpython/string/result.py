#student record 
def student(m1,m2,m3,m4):

    total=m1+m2+m3+m4
    avg=total/4
    print("Total of marks:",total,"/400")
    print("Average of your marks:",avg,"%")
a1=int(input("Enter your marks of subject_1:"))
a2=int(input("Enter your marks of subject_2:"))
a3=int(input("Enter your marks of subject_3:"))
a4=int(input("Enter your marks of subject_4:"))
student(a1,a2,a3,a4)
