import matplotlib.pyplot as plt
import pandas as pd
data=[['soham',19,92],['suhas',20,93],['sanket',21,89],['sagar',20,91],['sahil',25,90],['sidhant',22,87],['sudhir',24,67],['shailesh',21,85],['sumit',20,78],['shubham',23,74]]
df=pd.DataFrame(data,columns=['name','age','percentage'])
df.plot(x="name",y="percentage")
plt.show()
