# v0 Adnan Akbas
# V0.2 Bug fixed: Adnan, Mark, Dimitri, Ali, Colin
# v0.3 bug fixed: Adnan
from helpers import math_helper, pandas_helper

# 1. load vyntus,  activepal20, weight
respondent = 'BMR002'
activepal_df = pandas_helper.read_csv_activpal20(respondent).resample('30S').mean()
vyntus_df = pandas_helper.read_csv_vyntus(respondent)
respondents_df = pandas_helper.read_csv_respondents()

# cleaning vyntus data
vyntus_df['vyn_VO2'] = [float(vo2.replace(',', '.')) if type(vo2) == str else vo2 for vo2 in vyntus_df['vyn_VO2']]

vyntus_df = vyntus_df.resample('30S').mean()

# 2. combine vyntus("oxygenuptake") + activepal20("x","y","z" -> acceleration ), weight bades on time
met = vyntus_df.copy()[['vyn_VO2']]
met.dropna(how='any', subset=['vyn_VO2'], inplace=True)

met['weight'] = respondents_df.loc[float(respondent[3:6])]['gewicht']
met[['x', 'y', 'z']] = activepal_df.loc[met.index][['pal_accX', 'pal_accY', 'pal_accZ']]

# 3. create new column called met calculate values with oxygen and weight
met['acc'] = [math_helper.convert_to_acceleration(x, y, z) for x, y, z in zip(met['x'], met['y'], met['z'])]
met['met'] = [math_helper.calculate_met_value(vo2, weight) for vo2, weight in zip(met['vyn_VO2'], met['weight'])]

met.dropna(how='any', subset=['acc'], inplace=True)

met.to_csv('data/' + respondent + '/met.csv', date_format='%Y-%m-%d %H:%M:%S', index=True, header=True)
