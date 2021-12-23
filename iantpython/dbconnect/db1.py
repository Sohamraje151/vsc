import pymysql
con=pymysql.connect(
    host="localhost",
    user="soham",
    password="Sohamraje",
    database="soham")
if(not con==None):
    print("Success...!!!")
cmd=con.cursor()
# try:
# cmd.execute("insert into demo(id,name,addr,age)values(106,'prakash','kolkata',21)")
# con.commit()
cmd.execute("update demo set name='sumit',age=25 where id=106")
con.commit()
cmd.execute("select * from demo")
rs=cmd.fetchall()
for row in rs:
    print(row)
# except:
#     print("An Exception error occured...!!")
con.close()
