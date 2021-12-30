import pandas as pd
data=pd.read_csv("/home/student/Downloads/f.csv")

data['bmi']=None

b=data['weight']/(data['height'])**2
data['bmi']=b
print("------------------------------")

print(max(data['bmi']))
print(min(data['bmi']))
