# Program for sample python code for Z test
import math
import numpy as np
from numpy.random import randn
from statsmodels.stats.weightstats import ztest
mean_iq=110
sd_iq=15/math.sqrt(50)
null_mean=100
data=sd_iq*randn(50)+mean_iq
print('mean=%.2f stdv=%.2f'%(np.mean(data),np.std(data)))
ztest_Score,p_value=ztest(data,value=null_mean, alternative='larger')
if(p_value<0.05):
    print("Reject Null Hypothesis")
else:    
    print("fail to Reject Null Hypothesis")
