import pandas as pd
data=[['soham',19,'92%'],['soham',19,'92%'],['sanket',None,'89%'],['sagar',20,'90%'],[None,20,'90%']]
df=pd.DataFrame(data,columns=['name','age','percentage'])
df['remarks']=None
print("Original data:",df)
df.drop(columns='remarks',axis=1,inplace=True)
df.fillna("No Value Available",inplace=True)
print("Modified data:\n",df)

# ------output-------
'''
C:/Users/dell/vsc/ds/DS_assignments>python as1A6.py
Original data:      name   age percentage remarks
0   soham  19.0        92%    None
1   soham  19.0        92%    None
2  sanket   NaN        89%    None
3   sagar  20.0        90%    None
4    None  20.0        90%    None
Modified data:
                  name                 age percentage
0               soham                19.0        92%
1               soham                19.0        92%
2              sanket  No Value Available        89%
3               sagar                20.0        90%
4  No Value Available                20.0        90%
'''