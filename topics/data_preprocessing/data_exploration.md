## Created a script to look into activPAL data
I have created a script to look into data

script: [show_movement.py](../../evidence/python_script/show_movement.py)

# Created a script to plot data in 3d plot
I have created a script to plot data in 3d plot. It was unfortunately not useful.

script: [display_x_y_z.py](../../evidence/python_script/display_x_y_z.py)

# Looked into activities performed by participants

I have created a script that looks for all unique activities performed by participants

 | Dutch | English |
| ------ | ------ |
| lopen | walking |
| rennen |running |
| springen |jumping|
| staan | standing |
| traplopen | walking stairs |
| zitten | sitting|

script:  [activities_categories.pdf](../../evidence/python_notebook/activites_categories.pdf)


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

The functions are used by multiple different scripts to prepare the data for models.
Example: [all_steps_activity recognition_v3_analysis.pdf](../../evidence/all_steps_activity recognition_v3_analysis.pdf)