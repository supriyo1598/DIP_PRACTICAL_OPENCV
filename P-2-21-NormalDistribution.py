import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
np.random.normal()
# loc is mean, scale is std dev, size is count of samples
m=50
stddev=5
n = np.random.normal(loc=m, scale=stddev, size=10000)
n2 = np.random.normal(loc=m, scale=stddev+5, size=10000)
n,bins,patches=plt.hist(n, alpha=0.5, bins=20, density=True,color="green")
n2,bins2,patches2=plt.hist(n2, alpha=0.5, bins=20, density=True)
plt.title("Normal Distributions")
#plt.plot(range(len(bins)),bins)
plt.show();