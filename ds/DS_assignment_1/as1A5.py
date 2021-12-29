import pandas as pd
data=[['soham',19,'92%'],['soham',19,'92%'],['sanket',None,'89%'],['sagar',20,'90%'],[None,20,'90%']]
df=pd.DataFrame(data,columns=['name','age','percentage'])
df['remarks']=None
print("View null values:\n",df.isnull())
print("-------------------------------------")
print("Duplicate values:\n",df.duplicated())

# ----output-----
'''
C:/Users/dell/vsc/ds/DS_assignments>python as1A5.py
View null values:
     name    age  percentage  remarks
0  False  False       False     True 
1  False  False       False     True 
2  False   True       False     True 
3  False  False       False     True 
4   True  False       False     True 
-------------------------------------
Duplicate values:
0    False
1     True
2    False
3    False
4    False
dtype: bool
'''