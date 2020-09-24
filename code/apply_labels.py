## Adnan & Matthew - 9/17/2020

import os
from os import mkdir
from datetime import datetime
import pandas as pd


def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(float(timestamp.split(',')[0]))


def apply_labels(label_row, df_activpal):
    mask = (df_activpal.index >= label_row['start']) & (df_activpal.index <= label_row['stop'])
    df_activpal.loc[mask, "activity"] = label_row['activiteit']


def load_activapal(path):
    df = pd.read_csv(path, delimiter=';', header=0, index_col=0, parse_dates=True,
                     date_parser=timestamp_to_date)
    return df.resample('S').mean()


def load_activity(path):
    return pd.read_csv(path, delimiter=';', header=0, parse_dates=True)


# ----------------------------------------------------------------
def optimize_dataset(directory):
    df_actival = load_activapal('../data/'+directory + '/activpal20.csv')
    df_labels = load_activity('../data/'+directory + '/activiteiten.csv')

    for index, row in df_labels.iterrows():
        apply_labels(row, df_actival)

    mkdir('../out/' + directory)
    df_actival.to_csv('../out/' + directory + '/activepal.csv', index=True, header=True)


for directory in os.walk('../data'):
    if directory[0] == '../data':
        for subDirect in directory[1]:
            optimize_dataset(subDirect)