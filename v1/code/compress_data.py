# Adnan Akbas
import pandas as pd
import datetime


def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(float(timestamp.split(',')[0]))


data_src = '../data/BMR002/activpal20.csv'

df = pd.read_csv(data_src, delimiter=';', header=0, index_col=0, parse_dates=True, date_parser=timestamp_to_date)

df.count()

df_sampled_min = df.resample('S').mean()

df_sampled_min.to_csv('./out/active_pal_resampled_S.csv', index=True, header=True)
