# Program for two sample t-test
import statistics as st
import numpy as np
import scipy.stats as sc
d1=[11,16,6,17,12,13,8,15,14,9]
d2=[7,22,13,14,15,12,8,18,21,17,10,23]
mean1,mean2=st.mean(d1),st.mean(d2)
se1,se2=sc.sem(d1),sc.sem(d2)
sed=np.sqrt(se1**2.0+se2**2.0)
t_stat=(mean1-mean2)/sed
df=len(d1)+len(d2)-2
alpha=0.05
t_crit1=-2.09
t_crit2=+2.09
print("TOW SAMPLES t-TEST RESULTS")
print("..........................\n")
print("Standard error of two sample:",round(se1,2)," and ",round(se2,2))
print("Sample Mean of two Samples:",mean1," and ",mean2)
print("t-test:",round(t_stat,2))
print("t-critical:",round(t_crit1,2)," and ",round(t_crit2,2))
if(t_stat > t_crit1)and(t_stat<t_crit2):
    print("\nNull Hypothesis is accepted..!!")
else:
    print("\nNull Hypothesis is rejected..!!")
