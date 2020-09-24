import matplotlib.pyplot as plt
import pandas as pd
import math
from datetime import datetime

def convert_to_acceleration(row):
    return math.sqrt(row['pal_accX'] ** 2 + row['pal_accY'] ** 2 + row['pal_accZ'] ** 2)


def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(float(timestamp.split(',')[0]))


activepal = pd.read_csv('../../BMR002/activpal20.csv', delimiter=';', header=0, index_col=0, parse_dates=True,
                        date_parser=timestamp_to_date, nrows=1000000)

activepal['mag_accel'] = activepal.apply(lambda row: convert_to_acceleration(row), axis=1)

mask = (activepal.index > '2019-09-16 14:00:00') & (activepal.index < '2019-09-16 14:15:00')
df = activepal.loc[mask]

plt.figure(figsize=(60, 10))

plt.plot(df.index, df['mag_accel'], '.-')

plt.xticks(rotation=60)

plt.xlabel('Time', )
plt.ylabel('Magnitude Acceleration')
plt.title('3d visualization XYZ')

plt.show()
