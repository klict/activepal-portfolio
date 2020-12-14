# Data preparation

## descaled data and removed missing values
The descaling data happend in the function ``extract_features_from_correspondent`` while it's retrieving data and creating features from it
Removed missing values which can cause model fail happens at "Model preperation" phase of the script. 
 
 - [all_steps_activity recognition_v3_analysis.ipynb](../../evidence/all_steps_activity_recognition_v3_analysis.ipynb)

## features dataset
I have created a script that generates features dataset. It cuts raw dataset in time segment and calculates features. 
This script went through multiple versions.

- [all_steps_activity_recognition.ipynb](../../evidence/python_notebook/all_steps_activity_recognition.ipynb)
- [all_steps_activity_recognition_v2_analysis.ipynb](../../evidence/python_notebook/all_steps_activity_recognition_v2_analysis.ipynb)
- [all_steps_activity_recognition_v3_analysis.ipynb](../../evidence/python_notebook/all_steps_activity_recognition_v3_analysis.ipynb)

### features 
In the first version of this script i have created a function that calculates peak to peak distance of each axis.
In second and third version this was removed since there was no reason to use it and by removing it we have improved the model.

````python
def calculate_peak_distance(activpal_segment, key):
    accelerations = activpal_segment[key]

    # todo: Think about what kind peaks we are looking for and what we want to with it
    peak_index, _ = signal.find_peaks(accelerations)

    if len(peak_index) < 2:
        return 0

    peak_values = [accelerations[i] for i in peak_index]

    peak_values.sort(reverse=True)

    # There is a change there are is peak that shows up at multiple index
    # For this reason i am taking the index with highest value.
    highest_peak_index = activpal_segment[activpal_segment[key] == peak_values[0]].index.max()
    second_highest_peak_index = activpal_segment[activpal_segment[key] == peak_values[1]].index.max()

    diff_time = max(highest_peak_index, second_highest_peak_index) - min(highest_peak_index, second_highest_peak_index)

    # It's better to use microseconds diveded by 1000 to get milliseconds. This way you won't lose information
    # return diff_time.seconds * 1000
    return diff_time.microseconds / 1000

````

At the same time i have created small code to generate standard deviation and the mean of the y and z axis.
This piece of code was based on the code made by Matthew.

````python
    stdev_y =  statistics.stdev(activpal_segment['y']) if len(activpal_segment['y']) >= 2 else 0
    mean_y = activpal_segment['y'].mean()

    stdev_z =  statistics.stdev(activpal_segment['z']) if len(activpal_segment['z']) >= 2 else 0
    mean_z = activpal_segment['z'].mean()  

````

src: [all_steps_activity_recognition.ipynb](../../evidence/python_notebook/all_steps_activity_recognition.ipynb)

# time segment
The time segment is about how big of data we need to summerize in features.
When i say big i mean time range. In the development of model we saw that time segment has quite of influence of the model.

So I created a script that plots cross validation results over a wide time ranges. 
With model configuration how it was at the time we saw that 9.4 and 13 seconds gives the best result.

evidence: [all_steps_activity_recognition_v3_time_segment.ipynb](../../evidence/python_notebook/all_steps_activity_recognition_v3_time_segment.ipynb)


### balancing
While analysing the features dataset I had found that it was unbalanced. Certain activities had less data then others.
So i created a script that duplicates rows of each activity until all of them have equal amount
In the second of third version of this script it was removed,
because it would cause that model doesn't generalize on the activites with duplicated data.

````python
def balance_dataset_by_activity(dataset):
    highest_frequency  = dataset.groupby('activiteit').count()['standard_deviation_x'].max()
    unbalanced_dataset = dataset.copy()
    
    for activity_name in unbalanced_dataset.activiteit.unique():
        activity_data = unbalanced_dataset[unbalanced_dataset['activiteit'] == activity_name]
        
        multiplier =  int(highest_frequency / len(activity_data)) - 1
        unbalanced_dataset = unbalanced_dataset.append([activity_data] * multiplier, ignore_index=True)    
        
        activity_amount = len(unbalanced_dataset[ unbalanced_dataset['activiteit'] == activity_name])
        missing_amount = highest_frequency - activity_amount
        unbalanced_dataset = unbalanced_dataset.append(activity_data[:missing_amount], ignore_index=True)    

    return unbalanced_dataset
````

src: [all_steps_activity_recognition.ipynb](../../evidence/python_notebook/all_steps_activity_recognition.ipynb)

### converted activity string to binary category

This happens in each version of this script.

````python
features_dataset[activity_columns] = 0

features_dataset.loc[(features_dataset['activiteit'] == 'lopen'), 'activity_walking'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'rennen'), 'activity_running'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'springen'), 'activity_jumping'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'staan'), 'activity_standing'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'traplopen'), 'activity_traplopen'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'zitten'), 'activity_sitten'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'fietsen licht'), 'cycling_light'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'fietsen zwaar'), 'cycling_hard'] = 1

features_dataset.drop('activiteit', axis=1, inplace=True)
features_dataset.dropna(how='any', inplace=True)
````

src: [all_steps_activity_recognition_final_version.ipynb](../../evidence/python_notebook/all_steps_activity_recognition_final_version.ipynb)

### replaced NaN data with 0
Certain columns had data where it had value of NaN. 
To solve this we replaced it with zero but we later decided to remove these rows all together

````python
for column in features_columns[:-1]:
    features_dataset[column].fillna(0, inplace=True)
````
src: [all_steps_activity_recognition.ipynb](../../evidence/python_notebook/all_steps_activity_recognition.ipynb)