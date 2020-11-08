# V0 Adnan
# v0.2 fixed bugs

from helpers import math_helper, pandas_helper
import os
import pandas as pd

# 1. load vyntus,  activepal20, weight
respondents_df = pandas_helper.read_csv_respondents()


def create_met(respondent, activity='none', resample='30S'):
    activepal_df = pandas_helper.read_csv_activpal20(respondent).resample(resample).mean()
    vyntus_df = pandas_helper.read_csv_vyntus(respondent)

    if len(vyntus_df.index) == 0:
        return pd.DataFrame(index=pd.to_datetime([]))

    if activity != 'none':
        vyntus_df = vyntus_df[vyntus_df['vyn_activity'] == activity]

    # cleaning data
    vyntus_df['vyn_VO2'] = [float(vo2.replace(',', '.')) if type(vo2) == str else vo2 for vo2 in vyntus_df['vyn_VO2']]
    vyntus_df = vyntus_df.resample(resample).mean()

    # 2. combine vyntus("oxygenuptake") + activepal20("x","y","z" -> acceleration ), weight bades on time
    try:
        met = vyntus_df.copy()[['vyn_VO2']]
        met.dropna(how='any', subset=['vyn_VO2'], inplace=True)

        met['weight'] = respondents_df.loc[float(respondent[3:6])]['gewicht']
        met[['x', 'y', 'z']] = activepal_df.loc[met.index][['pal_accX', 'pal_accY', 'pal_accZ']]

        # 3. create new column called met calculate values with oxygen and weight
        met['acc'] = [math_helper.convert_to_acceleration(x, y, z) for x, y, z in zip(met['x'], met['y'], met['z'])]
        met['met'] = [math_helper.calculate_met_value(vo2, weight) for vo2, weight in
                      zip(met['vyn_VO2'], met['weight'])]

        met.dropna(how='any', subset=['acc'], inplace=True)

        met.to_csv('data/' + respondent + '/met.csv', date_format='%Y-%m-%d %H:%M:%S', index=True, header=True)

        print('saved :' + respondent)
        return met
    except Exception as e:
        print(e)
        return pd.DataFrame(index=pd.to_datetime([]))


comb_met_df = pd.DataFrame(index=pd.to_datetime([]))
activity = 'fietsen'
for directory in os.walk('data'):
    if directory[0] == 'data':
        for subDirect in directory[1]:
            if subDirect != 'BMR025':
                met = create_met(subDirect, activity=activity)
                comb_met_df = pd.concat([comb_met_df, met])

comb_met_df.to_csv('comb_met_' + activity + '.csv', date_format='%Y-%m-%d %H:%M:%S', index=True, header=True)
