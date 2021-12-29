import pandas as pd
data=[['soham',19,92],['suhas',20,93],['sanket',21,89],['sagar',20,91],['sahil',25,90],['sidhant',22,87],['sudhir',24,67],['shailesh',21,85],['sumit',20,78],['shubham',23,74]]
df=pd.DataFrame(data,columns=['name','age','percentage'])
print("Statistical Details of the data:\n--------------------------------\n",df.describe())

# -----------output-----------
'''
 C:/Users/dell/AppData/Local/Programs/Python/Python39/python as1A3.py         
Statistical Details of the data:
--------------------------------
             age  percentage
count  10.00000   10.000000
mean   21.50000   84.600000
std     1.95789    8.733079
min    19.00000   67.000000
25%    20.00000   79.750000
50%    21.00000   88.000000
75%    22.75000   90.750000
max    25.00000   93.000000
'''