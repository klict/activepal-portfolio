# Data Exploration

## Created a script to look into activpal data

This was the first script used to look into data. 

script: [show_movement.py](../../evidence/python_script/show_movement.py)

# Created a script to plot data in 3d plot
The idea was to see if plotting data in 3d plot would be useful and it was not the case
script: [display_x_y_z.py](../../evidence/python_script/display_x_y_z.py)

## Looked into activities performed by participants
 | Dutch | English |
| ------ | ------ |
| lopen | walking |
| rennen |running |
| springen |jumping|
| staan | standing |
| traplopen | walking stairs |
| zitten | sitting|

script:  [activities_categories](../../evidence/python_notebook/activites_categories.ipynb)

## Created some plots of activites of certain user
The target was to see patterns in activities and what the difference are between them

Examples: 
- Cycling: [cycling_bmr002.png](../../evidence/images/cycling_bmr002.png)
- Walking: [walking_bmr002.png](../../evidence/images/walking_bmr002.png)
- Sitting: [sitting_bmr002.png](../../evidence/images/sitting_bmr002.png)

# Helped in development of script to look into data and looked into it
I developed together with Matthew a small script that visualizes an activity for multiple users in one plot. 
This script was developed to help Matthew to find outliers and inconstancy in our dataset. 

````python
correspondents = ['BMR043']
#correspondents = ['BMR002', 'BMR004', 'BMR008', 'BMR012', 'BMR014', 'BMR015', 'BMR018', 'BMR031', 'BMR032', 'BMR033', 'BMR034','BMR036']
#correspondents = ['BMR040', 'BMR041', 'BMR042', 'BMR043', 'BMR044', 'BMR052', 'BMR053', 'BMR055', 'BMR058', 'BMR064', 'BMR097', 'BMR098', 'BMR099']
#correspondents = ['BMR002', 'BMR004', 'BMR008', 'BMR012', 'BMR014', 'BMR015', 'BMR018', 'BMR031', 'BMR032', 'BMR033', 'BMR034','BMR036', 'BMR040', 'BMR041', 'BMR042', 'BMR043', 'BMR044', 'BMR052', 'BMR053', 'BMR055', 'BMR058', 'BMR064', 'BMR097', 'BMR098', 'BMR099']

plt.figure(figsize=(25,10))
plt.title('G-Force in the activity standing still')
plt.xlabel('Time in 10 seconds intervals')
plt.ylabel('G-Force')

for corr in correspondents:
    activities_df = read_functions.read_activities(corr)
    
    start = activities_df.loc['zitten'].start
    stop = start + pd.DateOffset(seconds=180)
    
    activpal_df = activpal.read_data(corr, start, stop)

    activpal_df['x'] = convert_value_to_g(activpal_df['pal_accX'])
    activpal_df['y'] = convert_value_to_g(activpal_df['pal_accY'])
    activpal_df['z'] = convert_value_to_g(activpal_df['pal_accZ'])
    
    activpal_df.index = activpal_df.index.max() - activpal_df.index
   # print(activpal_df.head())
    activpal_df.dropna(inplace=True)
    
    if len(activpal_df) > 0:
        print(corr + "--",activpal_df.iloc[1].z)
    
    plt.plot(activpal_df.index, activpal_df.z, 'o-', label=corr)
    
plt.legend()

plt.show()
````
src: [analyse_and_document_x_y_z_data.ipynb](../../evidence/python_notebook/analyse_and_document_x_y_z_data.ipynb)
