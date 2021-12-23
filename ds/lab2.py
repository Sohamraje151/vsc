import pandas as pd
from scipy.stats import iqr
import matplotlib.pyplot as plt
data={'Name':['Geeta','Rani','Rohini','Rita','Rohan','Subham','Rishi','Ram','Dinesh','Arysn','Raja','Janavi'],'Marks':[73,58,75,85,51,65,87,74,53,47,89,75]}
dframe=pd.DataFrame(data)
dframe['Percentile_rank']=dframe.Marks.rank(pct=True)
print("Values of Percentile Rank in the Distribution")
print("______________________________________________")
print(dframe)
print("\nMeasures of Dispersion and Position in the Distribution")
print("__________________________________________________________")
rng=max(dframe["Marks"]) - min(dframe["Marks"])
print("Value of Range in the Distribution= ",rng)
std=round(dframe["Marks"].std(),3)
print("Value of Standard Deviation in the Distribution= ",std)
var=round(dframe["Marks"].var(),3)
print("Value of Varience in the Distribution= ",var)
iq=iqr(dframe["Marks"])
print("Value of Interquartile Range in the Distribution= ",iq)
print("\nBoxplot Repersentation of the Score1 Column")
print("_______________________________________________")
dframe.boxplot(column=["Marks"],grid=True,figsize=(7,7))
plt.text(x=0.75,y=dframe["Marks"].quantile(0.75),s="3rd Quartile")
plt.text(x=0.75,y=dframe["Marks"].median(),s="Median")
plt.text(x=0.75,y=dframe["Marks"].quantile(0.25),s="1st Quartile")
plt.text(x=0.75,y=dframe["Marks"].min(),s="Min")
plt.text(x=0.75,y=dframe["Marks"].max(),s="Max")
plt.text(x=0.6,y=dframe["Marks"].quantile(0.50),s="IQR",rotation=90,size=15)

