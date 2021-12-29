import pandas as pd
data=[['soham',19,'92%'],['suhas',20,'93%'],['sanket',21,'89%'],['sagar',20,'91%'],['sahil',25,'90%'],['sidhant',22,'87%'],['sudhir',24,'67%'],['shailesh',21,'85%'],['sumit',20,'78%'],['shubham',23,'74%']]
df=pd.DataFrame(data,columns=['name','age','percentage'])
print(df)


# ------output------
'''C:/Users/dell/vsc/ds/DS_assignments>python as1A1.py
       name  age percentage
0     soham   19        92%
1     suhas   20        93%
2    sanket   21        89%
3     sagar   20        91%
4     sahil   25        90%
5   sidhant   22        87%
6    sudhir   24        67%
7  shailesh   21        85%
8     sumit   20        78%
9   shubham   23        74%'''