# Data preparation

### peak-to-peak distance 
In the first version of this script, I have created a function that calculates peak to peak distance of each axis.
In the later versions, this function was removed since there was no reason to use it and by removing it I saw that model has improved.
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

src: [all_steps_activity_recognition.ipynb](../../evidence/python_notebook/all_steps_activity_recognition.ipynb)

# time segment
The time segment is about how much data we need to summarize with features.
 In the development of the model, I saw that time segment choice has quite of influence on the model prediction ability.

So I created a script that helps with selecting a time segment:



evidence: [all_steps_activity recognition_final_version_split_cycling_time_segment.ipynb](../../evidence/python_notebook/all_steps_activity recognition_final_version_split_cycling_time_segment.ipynb)


### balancing
While analysing the features dataset, I have found that it was unbalanced. Certain activities had less data than others.
So I created a script that duplicates rows of each activity until all of them have an equal amount of data points.
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