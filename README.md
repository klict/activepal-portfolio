# portfolio
naam: Adnan Akbas
studentnummer: 17005116

## Project ActivPal

### Team members
- Ali
- Colin
- Mark
- Matthew


## Datacamp
  ![Image that shows overview of completed courses](evidence/images/datacamp.PNG)

 |Course|Statement of Accomplishment|
 |------|---------------------------|
 | Introduction to python |[proof](evidence/datacamp/introduction_to_python.pdf)|
 | Python Data Science Toolbox (Part 1) |[proof](evidence/datacamp/python_data_science_toolbox_part_1.pdf)|
 | Intermediate Python |[proof](evidence/datacamp/intermediate_python.pdf)|
 | Python Data Science Toolbox (Part 2) |[proof](evidence/datacamp/python_data_science_toolbox_part_2.pdf)|
 | Pandas Foundations |[proof](evidence/datacamp/pandas_foundations.pdf)|
 | Introduction to Data Visualization in Python |[proof](evidence/datacamp/introduction_to_data_visualization_in_python.pdf) |
 | Manipulating Dataframes with pandas |[proof](evidence/datacamp/manipulating_dataframes_with_pandas.pdf)|
 | Data Types for Data Science in Python |[proof](evidence/datacamp/data_types_for_data_science_in_python.pdf)|
 | Cleaning data in Python |[proof](evidence/datacamp/cleaning_data_in_python.pdf)|
 | Preprocessing for Machine Learning in Python |[proof](evidence/datacamp/preprocessing_for_machine_learning_in_python.pdf)|

### Research project
<details> <summary>Task Definition</summary>

In the research plan I have written the second iteration of the problem domain/context while my teammates have worden on other parts. 
Where they have defined the research question among others. In the second iteration I have processed the feedback we got
from one of our teachers. 

``
Statistics Netherlands (CBS) has the wish to see if their respondents are moving for at least 150
minutes per week in moderately intense physical activity.
Currently, they are measuring by asking their respondent or health surveys. The issue with this is
that people are not very good at estimating the time they spent on moving and sport. This of course
causes that they don't have very reliable data to work with. Therefor CBS has been looking into
alternatives like the ActivPal accelerometer in combination with machine learning to give better and
more accurate results when measuring the intensity of certain activities.
Because of this the CBS started to collect lab tests and started to measure the movements of 41
correspondents in their regular workweek by using the Activepal Accelerator. It's our job to analyse,
structure and build machine learning algorithms based on the collected data to see if we can
determine if people adhere to (inter)national norm for physical activities and if we could measure
the intensity of movement (without the heart rate information).
``

src: [research_plan.pdf](evidence/documents/research_plan.pdf)

</details>

<details> <summary>Evaluation</summary>

[More Examples](topics/research_project/evaluation.md)

</details>

<details> <summary>Conclusions</summary>

[More Examples](topics/research_project/conclusions.md)

</details>

<details> <summary>Planning</summary>

At the beginning of our project we have decided that we will use Jira as our scrum board and will implement Scrum in our way and won't follow it to the detail.
Our group was based on trust that's also the reason why we didn't setup nor sign a contract for teamwork. 

Our process looked as following. At the start of each sprint we decided what goal is for the sprint. With this goal in mind we created task which each team member could choose and take it on themself.
The task can be modified, removed or created while the sprint were going onbut that was always first discussed within the group before any modification.
Each morning at 9:30 our group was holding a stand-up. There we discussed what we did day earlier, going to do today and if we are stuck with something.
At the end of each sprint our group was holding retrospective where we discussed our progress and teamwork last sprint. The role of scrum master was taken on by Ali Safdari. 

## My role in scrum
I didn't have specific role in the scrum process other than developer but i did actively participate in each phase of 
the scrum process.At the sprint planning I have actively created task of course after discussing with the team. At the 
same time I would assign task to myself unless other team members would want them. In some cases we would assign 
multiple members to a task. Unfortunately Jira doesn't support that so we would write the names in description of the task.
Each morning I would join stand-up with my other team members and explain what i did yesterday, what i am gonna do today and if i need help.
Unfortnatly and reasonably we didn't take notes so I don't have evidence for this. At the end of each sprint I would 
join retrospective and give my input. I would say what we did well, what didn't go well and what i wish next sprint would get better.

[More information on our take](topics/research_project/planning.md)

</details>

### Domain knowledge
<details> <summary>Introduction of the subject field</summary>

[More Examples](topics/domain_knowledge/introduction_of_the_subject_field.md)

</details>

<details> <summary>literature Research</summary>

[More Examples](topics/research_project/literature_research.md)

</details>

<details> <summary>Explanation of Terminology, jargon and definitions</summary>

[More Examples](topics/research_project/explanation_of_terminology_jargon_and_definitions.md)

</details>

### Data preprocessing
<details> <summary>Data exploration</summary>

While working on the Activity Recognion model I have explored data in certain way. 
I tried to get an idea if there was a pattern in my dataset. If i say pattern i mean that the acceleration
data looks in a certain way for activity. The image below does show it quite clearly that each activity has hiw own pattern.

![Image that shows plots which show in turn patterns of each activity](evidence/images/combination.png)


[More Examples](topics/data_preprocessing/data_exploration.md)

</details>

<details> <summary>Data cleaning</summary>

Our dataset was provided by CBS in cleaned state. This means they already cleaned it for us and that there wasn’t much 
for us to do.. While I say this we did find certain issues while working on our models. My teammates  found out that 
following respondents data were not there or corrupt:

Cases:
-	BMR060 didn't have vyntus.csv file. This file contains oxygen intake which is need for calculating MET-value.
-	BMR025 activities that are logged doesn't show up in the data
-	BMR035 activities that are logged doesn't show up in the data
-	BMR100 activities that are logged doesn't show up in the data
-	BMR051 activities that are logged doesn't show up in the data
-	BMR027 activities that are logged doesn't show up in the data

Other than this we finally found thanks to the help of a teacher what actually the acceleration data means.  
He explained to us that it was scaled so that ActivPal device could keep much more records than it originally could. 
He gave us a formula that would convert scaled value back to  Gravitational acceleration. I have implemented this 
formula in Python as shown as below:

```` python
def convert_value_to_g(value):
    return (value - 127) / 63
````

evidence: [math_helper.py](evidence/python_script/math_helper.py)


[More Examples](topics/data_preprocessing/data_cleaning.md)

</details>

<details> <summary>Data preparation</summary>

I have developed almost all of the data preparation code for Activity Recognition model. First I have developed a 
function that extracts features from accelerometer dataset of an respondent. In this function we are creating new features which summerizes a certain time range.
I specificaly created the features standard deviation and mean of Y and Z axis. Mathew worked on the features mean and standard deviation of the X axis. I have also created peace of code that calculates
peak-to-peak distance but I have removed in favor better features. By removing I saw improvement at the time. At the end I am also removing any rows that has null values.

````python
def extract_features_from_correspondent(correspondent):
    features_df = pd.DataFrame(columns=features_columns, index=pd.to_datetime([]))

    # Getting dataset for a correspodent
    activities_df = read_functions.read_activities(correspondent)
        
    for activity_name in activities:
        activity = activities_df.loc[activity_name]
        if not activity.empty:
            start_time = activity.start
            stop_time = activity.stop
            activpal_df = activpal.read_data(correspondent, start_time, stop_time)

            # denormalizing dataset
            activpal_df['x'] = math_helper.convert_value_to_g(activpal_df['pal_accX'])
            activpal_df['y'] = math_helper.convert_value_to_g(activpal_df['pal_accY'])
            activpal_df['z'] = math_helper.convert_value_to_g(activpal_df['pal_accZ'])

            date_range = pd.date_range(start_time, stop_time, freq=str(segment_size) + 'S')
            
            for time in date_range:
                segment_time = time + pd.DateOffset(seconds=segment_size)
                activpal_segment = activpal_df[(activpal_df.index >= time) & (activpal_df.index < segment_time)]

                stdev_x =  statistics.stdev(activpal_segment['x']) if len(activpal_segment['x']) >= 2 else 0
                mean_x = activpal_segment['x'].mean()

                stdev_y =  statistics.stdev(activpal_segment['y']) if len(activpal_segment['y']) >= 2 else 0
                mean_y = activpal_segment['y'].mean()

                stdev_z =  statistics.stdev(activpal_segment['z']) if len(activpal_segment['z']) >= 2 else 0
                mean_z = activpal_segment['z'].mean()  


                features_df.loc[segment_time] = [stdev_x, mean_x, stdev_y, mean_y, stdev_z, mean_z, activity_name]

    features_df.dropna(how='any', inplace=True)

    return features_df
````

I have also developed functions that makes it easier to create one dataset where all features dataset from respondents merged.

````python
def extract_features_from_correspondents(correspodents):
    all_features_df = pd.DataFrame(index=pd.to_datetime([]))

    for correspodent in correspodents:
        print("Extracting " + correspodent)
        
        features_df     = extract_features_from_correspondent(correspodent)
        all_features_df = pd.concat([all_features_df, features_df])
    
    print("Done extracting features")

    return all_features_df

def extract_features_from_all_correspondents(exclude_test_correspodent = True):
    
    exclude_directory = ['output', 'throughput', 'Test data','.ipynb_checkpoints']
    exclude_respodents = ['BMR015','BMR025','BMR027', 'BMR035', 'BMR051', 'BMR054', 'BMR060', 'BMR099', 'BMR100']
    
    exclude = exclude_respodents + exclude_directory
    
    if (exclude_test_correspodent):
        exclude = exclude + test_users
    
    correspodents = []
    
    for directory in os.walk('../../data'):
        if directory[0] == '../../data':
            correspodents = directory[1]
            
    for exclude_item in exclude:
        if exclude_item in correspodents:
            correspodents.remove(exclude_item)
        
    return extract_features_from_correspondents(correspodents)
```` 

As last I have written a peace of code that converts activity labels to numbers so that the model can use it.

````python
features_dataset[activity_columns] = 0

#features_dataset.loc[(features_dataset['activiteit'] == 'springen'), 'activity_jumping'] = 1
#features_dataset.loc[(features_dataset['activiteit'] == 'traplopen'), 'activity_traplopen'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'lopen'), 'activity_walking'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'rennen'), 'activity_running'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'staan'), 'activity_standing'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'zitten'), 'activity_sitten'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'fietsen licht'), 'activity_cycling_light'] = 1
features_dataset.loc[(features_dataset['activiteit'] == 'fietsen zwaar'), 'activity_cycling_heavy'] = 1

features_dataset.drop('activiteit', axis=1, inplace=True)
````


All of the provided code can be found in each of these python notebooks below:
- [all_steps_activity recognition_final_version_split_cycling_12_1_seconds]()
- [all_steps_activity recognition_final_version_split_cycling_8_9_seconds]()
- [all_steps_activity recognition_final_version_split_cycling_7_seconds]()
 






[More Examples](topics/data_preprocessing/data_preparation.md)

</details>

<details> <summary>Data visualization</summary>
To get an idea what kind of features we could use other than what the paper “” suggest I did some research into our data. 
I made a line plot for each activity for different respondents.  The image below shows clearly that each activity has 
a unique pattern. So with this information I concluded that we may not need peak-to-peak feature and just could use 
standard deviation and mean of each axis. The paper suggested different  features but at the end we only used  the 
suggested feature mean and standard deviation of the X-axis and dropped peak-to-peak feature. The scale of Y-axis at 
the time of decision didn’t really matter much because the pattern would still be the same. 
We did still descale it back gravitional acceleration at the end.  

![Image that shows plots which show in turn patterns of each activity](evidence/images/combination.png)


[More Examples](topics/data_preprocessing/data_visualization.md)

</details>

<details> <summary>Data explanation</summary>

In the paper I have written the first version of subchapter subjects of chapter data where I describe the characteristics of our subject. Also I have written  subchapter study design of chapter data  where I describe how the data is recorded in the lab.   

CBS provided us ActivPAL accelerometer dataset, Vytnus dataset and activity log file of each of 31 respondents . They also provided us data from other devices but these were not used in our project. We also got an excel file where they described characteristics of the respondents.  
  
**Activity log dataset**
This dataset was used  for devloping both MET-regression en activity recognition models. In the case of Activity recognition models it was used to label accelerometer data.

| column | datatype | description| 
|--|--|--|
 activiteit| text | the name of an activity| 
| start| text |The date and time when an activity was started  | 
| stop| text|The date and time when an activity ended | 

**Vyntus  dataset**  
  
Vyntus is an device which analyzes  breathing of a person. The Vyntus dataset contains allot of features but we only used specifick features in the MET-regression models 
  
| column | datatype | description|   
|--|--|--|  
|vyn_time| timestamp| The date and time when breathing is analyzed |   
| vyn_VO2 | int | rate of oxygen consumption | 

**ActivPAL dataset**  
  This dataset was both used to develop both MET-regression and activity recognition models

| column | datatype | description|   
|--|--|--|  
|pal_time| timestamp| The date and time when accelerometer data is recorded |   
| pal_accX| int | scaled value of gravitational acceleration of the X axis | 
| pal_accY| int | scaled value of gravitational acceleration of the Y axis | 
| pal_accZ| int | scaled value of gravitational acceleration of the Z axis | 
</details>


### Predictive Analytics

<details> <summary>selecting a model</summary>

[More Examples](topics/data_preprocessing/selecting_a_model.md)

</details>

<details> <summary>training model</summary>

[More Examples](topics/data_preprocessing/training_model.md)

</details>

<details> <summary>evaluating a model</summary>

[More Examples](topics/data_preprocessing/evaluating_a_model.md)

</details>

<details> <summary>Visualizing the outcome of a model</summary>

[More Examples](topics/data_preprocessing/visualizing_the_outcome_of_a_model.md)

</details>

<details> <summary>configuring a model</summary>

[More Examples](topics/data_preprocessing/configuring_a_model.md)

</details>

### communication
<details> <summary>presentation</summary>

| Week | Contrubition | Link |
|------|--------------|------|
|1|No presentation||
|2|Contributed to the presentation by adding content to dia 5|[Week 2 presentation](evidence/presentations/week_2_internal.pdf)|
|3|Contributed to the presentation by adding content to dia 4 and I gave the presentation.|[Week 3 presentation](evidence/presentations/week_3_internal.pdf)|
|4|Contributed to the presentation by adding content to dia 2, 3, 12 and 13|[Week 4 presentation](evidence/presentations/week_4_external.pdf)|
|5|Contributed to the presentation by adding content to dia 3|[Week 5 presentation](evidence/presentations/week_5_internal.pdf)|
|6|Contributed to the presentation by adding content to dia 4, 5 and 6|[Week 6 presentation](evidence/presentations/week_6_internal.pdf)|
|7|Contributed to the presentation by adding content to dia 6 and I gave the presentation.|[Week 7 presentation](evidence/presentations/week_7_internal.pdf)|
|8|Contributed to the presentation by adding content to dia 8, 9, 10 and 11.|[Week 8 presentation](evidence/presentations/week_8_external.pdf)|
|9|Contributed to the presentation by adding content to dia 4.| [Week 9 presentation](evidence/presentations/week_9_internal.pdf)|
|10|Contributed to the presentation by adding content to dia 5 with Ali Safdari| [Week 10 presentation](evidence/presentations/week_10_internal.pdf)|
|11|Contributed to the presentation by adding content to dia 4.| [Week 11 presentation](evidence/presentations/week_11_internal.pdf)|
|12||
|13|Contributed to the presentation by adding content to dia 4.| [Week 13 presentation](evidence/presentations/week_13_external.pdf)|
|14|Contributed to the presentation by adding content to dia 4 and I gave the presentation| [Week 14 presentation](evidence/presentations/week_14_internal.pdf)|
|15|I didn't contribute anything | [Week 15 presentation](evidence/presentations/week_15_internal.pdf)|
|16| | [Week 16 presentation](evidence/presentations/week_16_external.pdf)|
|17|  | [Week 17 presentation](evidence/presentations/week_17_internal.pdf)|



</details>

<details> <summary>writing paper</summary>

|Contribution|Iteration|Chapter|Link|
|------------|---------|-------|----|
|Wrote 1e iteration together with Ali Safdari. I tried to write it alone but I couldn't put the infromation about the method in the right way. Ali wrote the text while I told him what needs to be in the paper.|1| Subchapter activity recognition of chapter method|[1e iteration of subchapter acitivity recognition chapter method](evidence/paper_chapters/method_activity_recognition_version_1.pdf)|
|Processed feedback from my teammates |2| Subchapter activity recognition of chapter method|[2e iteration of subchapter acitivity recognition of chapter method](evidence/paper_chapters/method_activity_recognition_version_2.pdf)|
|Processed feedback from my teammates |3| Subchapter activity recognition of chapter method|[3e iteration of subchapter acitivity recognition of chapter method](evidence/paper_chapters/method_activity_recognition_version_3.pdf)|
|Wrote 1e iteration |1| Subchapter activity recognition of chapter result|[1e iteration of subchapter acitivity recognition of chapter result](evidence/paper_chapters/result_activity_recognition_version_1.pdf)|
|Processed feedback from my teammates|2| Subchapter activity recognition of chapter result|[2e iteration of subchapter acitivity recognition of chapter result](evidence/paper_chapters/result_activity_recognition_version_2.pdf)|
|Processed feedback from my teammates|3| Subchapter activity recognition of chapter result|[3e iteration of subchapter acitivity recognition of chapter result](evidence/paper_chapters/result_activity_recognition_version_3.pdf)|
|Wrote 1e iteration |1|subchapter study design of chapter data|[1e iteration of subchapter study design of chapter data](evidence/paper_chapters/data_study_design_version_1.pdf)|
|Wrote 1e iteration |1|subchapter subjects of chapter data|[subchapter subjects of chapter data](evidence/paper_chapters/data_subjects_version_1.pdf)|

</details>




