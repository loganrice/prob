import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

plt.figure()
plt.hist(x, histtype='bar')
plt.savefig("./graphs/histogram.png")

plt.figure()
plt.boxplot(x)
plt.savefig("./graphs/boxplot.png")

plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("./graphs/qq-plot-normal.png")

plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("./graphs/qq-plot-non-normal.png")
