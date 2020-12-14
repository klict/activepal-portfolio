#V1 Adnan

from helpers import math_helper, pandas_helper
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. load vyntus,  activepal20, weight
respondent = 'BMR002'
activepal_df = pd.read_csv('comb_met_lopen.csv', delimiter=',', index_col=0, parse_dates=True)

x = activepal_df['acc'].values.reshape(-1, 1)
y = activepal_df['met']

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)

print(r_sq)

plt.plot(activepal_df['x'], activepal_df['met'], 'o')
plt.title('comb_met')
plt.xlabel('Acceleration (m/s2)')
plt.ylabel('MET(Methobolic equivelant of task)')

m, b = np.polyfit(activepal_df['acc'], activepal_df['met'], 1)

plt.plot(activepal_df['x'], m * activepal_df['x'] + b)
plt.show()
