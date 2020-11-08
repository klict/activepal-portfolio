# Data preparation
In our case the data was already cleaned by cbs.
But we did find certain participants didn't have the certain data or it was corrupt.

Cases:
- BMR060 didn't have vyntus.csv file. This file contains oxygen intake which is need for calculating MET-value.
- BMR025 activities that are logged doesn't show up in the data
- BMR035 activities that are logged doesn't show up in the data
- BMR100 activities that are logged doesn't show up in the data
- BMR051 activities that are logged doesn't show up in the data
- BMR027 activities that are logged doesn't show up in the data

The issues came up while developing models, so we excluded them from developing dataset.

Scripts:  
 - [all_steps_activity recognition_v3_analysis.ipynb](evidence/all_steps_activity recognition_v3_analysis.ipynb)
 - [intensity_classification_model.ipynb](evidence/intensity_classification_model.ipynb)  

# Created functions that is used to convert data

Convert x, y and z-axis acceleration to magnitude of acceleration

```` python
def convert_to_acceleration(row):
    return math.sqrt(row['pal_accX'] ** 2 + row['pal_accY'] ** 2 + row['pal_accZ'] ** 2)
````

Created a function to calculate MET-value from oxygen intake and weight

```` python
def calculate_met(vo2, kg):
    return vo2 / (3.5 * kg)
````

Created a function that descales g-force. Activpal record data inunsigned integers to maximaze recodable data. 
We need to convert this data to G-force which we understand and can use.

```` python
def convert_value_to_g(value):
    return (value - 127) / 63
````

evidence: [math_helper.py](evidence/math_helper.py)

The functions are used by multiple different scripts to prepare the data for models:
Example: [all_steps_activity recognition_v3_analysis.ipynb](evidence/all_steps_activity recognition_v3_analysis.ipynb)
