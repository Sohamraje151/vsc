import  matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("/home/student/Downloads/f.csv")
data.plot.scatter(x='height',y='weight')
plt.show()

