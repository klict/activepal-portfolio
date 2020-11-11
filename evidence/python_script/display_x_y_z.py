import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file = './out/active_pal.csv'

df = pd.read_csv(file, header=0, index_col=0, parse_dates=True)

fig = plt.figure(figsize=(12, 9))
ax = Axes3D(fig)

xData = df['pal_accX']
yData = df['pal_accY']
zData = df['pal_accZ']

ax.scatter(xData, yData, zData)

plt.title('3d visualization XYZ')

ax.set_ylabel('Y')
ax.set_xlabel('X')
ax.set_zlabel('Z')

plt.show()