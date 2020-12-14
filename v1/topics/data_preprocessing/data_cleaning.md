# Data cleaning
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
 - [all_steps_activity recognition_v3_analysis.ipynb](../../evidence/python_notebook/all_steps_activity_recognition_v3_analysis.ipynb)
 - [intensity_classification_model.ipynb](../../evidence/python_notebook/intensity_classification_model.ipynb)  

# Created functions that is used to convert data

Convert x, y and z-axis acceleration to magnitude of acceleration

```` python
def convert_to_acceleration(row):
    return math.sqrt(row['pal_accX'] ** 2 + row['pal_accY'] ** 2 + row['pal_accZ'] ** 2)
````


Created a function that descales value from activpal to G-force. Activpal inherintly records data in unsigned format to be able record huge amount of data.
So we need to descale this to get actually usable data.

```` python
def convert_value_to_g(value):
    return (value - 127) / 63
````

evidence: [math_helper.py](../../evidence/python_script/math_helper.py)

The functions are used by multiple different scripts to prepare the data for models:
Example: [all_steps_activity recognition_v3_analysis.ipynb](evidence/all_steps_activity recognition_v3_analysis.ipynb)
