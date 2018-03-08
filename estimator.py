import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import plotly.plotly as py
paths=["0_5_cc.csv","2cc.csv","cc.csv"]

matrix_mean=[]
matrix_std=[]
for path in paths:
    df= pd.read_csv("./"+path)
    mean=list(df.mean(axis=0))
    std=list(df.std(axis=0))
    matrix_std.append(std)
    matrix_mean.append(mean)

# for i in range(0,3):
#     plt.plot(matrix_mean[i],'r--')
#     plt.plot([x + 3*y for x, y in zip(matrix_mean[i], matrix_std[i])],'b--')
#     plt.plot([x - 3*y for x, y in zip(matrix_mean[i], matrix_std[i])],'g--')
#
#     plt.show()

fig = plt.figure()

list_1an=list(df[df.columns[-1]])
mu=np.mean(list_1an)
sigma=np.std(list_1an)
plt.hist(list_1an,bins=500)

plt.show()
# print(np.mean(list_1an))
# gaussian_approximation=np.random.normal(loc=np.mean(list_1an),scale=np.std(list_1an),size=1000)
x = np.linspace(min(list_1an), max(list_1an), 100)
plt.plot(x,mlab.normpdf(x, mu, sigma))


plt.show()