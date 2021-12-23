# Program for Paired sampled t-test
import statistics as st
import numpy as np
import math
d1=[3.8,5.2,3.9,4.1,4.3,4.4,4.2,5.6]
n=10
s_mean=st.mean(d1)
sd=0
for e in d1:
    sd=sd+(float(e)-s_mean)**2
sigma=math.sqrt(sd/(n-1))
den=sigma/np.sqrt(n)
num=s_mean-4
t_stat=num/den
alpha=0.05
t_crit1=-2.262
t_crit2=+2.262
print("TOW SAMPLES paired t-TEST RESULTS")
print("..........................\n")
print("sample mean:",s_mean)
print("Standard deviation:",round(sigma,2))
print("t-test:",round(t_stat,2))
print("t-critical:",round(t_crit1,2)," and ",round(t_crit2,2))
if(t_stat > t_crit1)and(t_stat<t_crit2):
    print("\nNull Hypothesis is accepted..!!")
else:
    print("\nNull Hypothesis is rejected..!!")
