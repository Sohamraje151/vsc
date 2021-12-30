import pandas as pd
data=pd.read_csv("/home/student/f.csv")
print("\nFirst 10 rows:\n----------------------------------\n",data.head(10))
print("\nLast 10 rows:\n----------------------------------\n",data.tail(10))
print("\nRandom 20 rows:\n----------------------------------\n",data.sample(20))

