import pandas as pd
data=[['soham',19,'92%'],['soham',19,'92%'],['sanket',None,'89%'],['sagar',20,'90%'],[None,20,'90%']]
df=pd.DataFrame(data,columns=['name','age','percentage'])
df['remarks']=None
print(df)

# ----------output------------
'''C:/Users/dell/AppData/Local/Programs/Python/Python39/python as1A4.py
     name   age percentage remarks
0   soham  19.0        92%    None
1   soham  19.0        92%    None
2  sanket   NaN        89%    None
3   sagar  20.0        90%    None
4    None  20.0        90%    None
'''
