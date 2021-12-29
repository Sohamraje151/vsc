import pandas as pd
data=[['soham',19,'92%'],['suhas',20,'93%'],['sanket',21,'89%'],['sagar',20,'91%'],['sahil',25,'90%'],['sidhant',22,'87%'],['sudhir',24,'67%'],['shailesh',21,'85%'],['sumit',20,'78%'],['shubham',23,'74%']]
df=pd.DataFrame(data,columns=['name','age','percentage'])
print("Original Data:\n",df)
print("-------------------------------------")
print("Shape of Data:\n",df.shape)
print("-------------------------------------")
print("Number of Rows-Columns:\n",df.size)
print("-------------------------------------")
print("Data-types:\n",df.dtypes)
print("-------------------------------------")
print("Feature names:\n",df['name'].value_counts())
print("-------------------------------------")
print( "Description of data:")
print(df.info())

# ------------output-------------
'''C:/Users/dell/vsc/ds/DS_assignments>python as1A2.py
Original Data:
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
9   shubham   23        74%
-------------------------------------
Shape of Data:
 (10, 3)
-------------------------------------
Number of Rows-Columns:
 30
-------------------------------------
Data-types:
 name          object
age            int64
percentage    object
dtype: object
-------------------------------------
Feature names :
soham       1
suhas       1
sanket      1
sagar       1
sahil       1
sidhant     1
sudhir      1
shailesh    1
sumit       1
shubham     1
Name: name, dtype: int64
-------------------------------------
Description of data:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 3 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   name        10 non-null     object
 1   age         10 non-null     int64
 2   percentage  10 non-null     object
dtypes: int64(1), object(2)
memory usage: 368.0+ bytes
None'''