import pandas as pd
data=pd.read_csv("/home/student/Downloads/f.csv")
print(data)
data['bmi']=None

b=data['weight']/(data['height'])**2
data['bmi']=b
print("------------------------------")
print(data)
