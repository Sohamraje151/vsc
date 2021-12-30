import pandas as pd
data=pd.read_csv("/home/student/f.csv")
print("Number of Observations:\n",data.info())
print(data.isnull())
data.fillna('NaN',inplace=True)
print(data)