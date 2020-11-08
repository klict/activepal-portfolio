# Improving the assessment of daily energy expenditure by identifying types of physical activity using a single accelerometer

## Paper notes:

The ADD of the identified activity types was used for the assessment of PA by defining a daily metabolic equivalent value (METD). The METD was calculated as the mean of the standard metabolic equivalent value (MET) of each activity type weighed by the ADD, as shown in the equation below

**Formule description:**

- I is an index that corresponds to each of the 6 activity types
- METi is the standard MET value for the i-activity
- K represents the number of monitoring minutes during the day
- is the average daily duration of an activity type. It was calculated as the total duration of each activity divided by the number of monitoring days

**Dataset notes:**

- According to the diaries, the non-wearing time during waking hours was removed from the dataset

**Classification tree**

**Steekproef grootte:**

- **40 personen**
  - **20 man**
  - **20 vroew**

Supervised test including lying, sitting, standing still, walking, running, cycling, dishwashing and floor-sweeping.

Acceleration collected during the dishwashing and floor-sweeping were used to define the **AS** category.

Acceleration collected during sitting and standing still were used to define the Sit-Stand category. These two activities have been grouped together to form a single category because the use of one accelerometer to measure PA did not allow the accurate distinction of the sitting and standing still postures

**Categories**

| Lie |
 |
| --- | --- |
| Run |
 |
| Walk |
 |
| AS | Dishwashing, floot-sweeping |
| Cycle |
 |
| Sit-Stand | Stting and standing |

Features:

| the standard deviation of the acceleration in the vertical |
| --- |
| medio-lateral directions of the body |
| the average acceleration in the vertical direction of the body |
| the peak-to-peak distance of the acceleration measured in the medio-lateral, and antero-posterior direction of the body |
| the frequency peak of the power spectral density of the acceleration measured in the vertical direction of the body |

Secondly, the raw acceleration signal was processed to identify types of PA performed during the day. The acceleration signal was segmented in nonoverlapping intervals of 6.4 seconds. This segment length was selected because the accuracy of classification models used to identify activity types could decrease when the acceleration signal is analyzed in portion of shorter time length (10). In each segment of the acceleration and for each sensing axis, the following acceleration features were determined: average, standard deviation, peak-to-peak distance, and dominant frequency in the power spectral density. Because of the high accuracy in identifying activity types (10, 11), a classification tree algorithm was employed to evaluate the features and to classify the acceleration in one of 6 activity classes: &quot;lie&quot;, sitting or standing (&quot;Sit-Stand&quot;), active standing (&quot;AS&quot;), &quot;walk&quot;, &quot;run&quot; and &quot;cycle&quot;.

# Detection of type, duration and intensity of physical activity using an accelerometer

Notes on Abstract:

- 20 subjects performed 20 activities
- Tri-axial accelerometer mounted on lower back
- Identification of activity type was based on a decision tree
  - Evaluated attributes (features) of activity signal
  - Features were measured in intervals of defined duration(segments)
  - Segment determined the time resolution of 0.4, 0.8, 1.6, 3.2, 6.4 and 12.8
  - Each segment size was evaluated
- Multiple-linear regressions were used to estimate speed of walking, running and cycling based on acceleration

**Experimental Methods:**

Activities

| lying on a bed | sitting on a chair | sitting while working on a compute |
| --- | --- | --- |
| standing | standing washing dishes | walking along a corridor |
| walking outdoors | running outdoors and cycling | walking downstairs and walking upstairs |

Data processing:

- The acceleration signal of each activity task was isolated according to the starting and the finishing time as recorded with the stopwatch
- Valid data for each task: start time + 5 sec \&lt;\&gt; end time – 5
  - These 5 second times delay was set to analyze only data recorded during a stationary state for each activity, and it was determined by visual inspection of the dataset
- The isolated signal was then used to calculate features
- Accurate assessment of activity duration requires analysis in small segment, but larger segment would
  - 0.4, 0.8, 1.6, 3.2, 6.4 and 12.8 seconds including 8, 16, 32, 64, 128, and 256 samples
- Acceleration signal stored in each segment was processed to extract features in the time and frequency domain
- Features Time domain
  - Average
  - the standard deviation
  - Peak-to-peak distance
  - the cross-correlation (R) of the acceleration between sensing axes
    - This feature provided a measure of the similarity in the acceleration over two subsequent time intervals for the same axis
- the power spectral density (P) of the acceleration was used to define the harmonic content of the signal. P was calculated using the fast Fourier transform algorithm on the acceleration signal of each segment
- Features frequency domain:
  - Dominant frequency
    - The dominant frequency was the frequency at which P had the maximum value.
  - the amplitude of the spectral peak (A)
    - The A was defined as the maximum value of P
  - the frequency domain entropy (J)
    - J was defined as in Equation 3.

Equations: the cross-correlation (R) of the acceleration between sensing axes

![](RackMultipart20201021-4-yfphtk_html_c3eedf6315fc3db3.png)

- α and β represent two subsequent segments of the same axis
- i is the shift between the two segments
- J is an index that covers the full length of the overlapping samples between α and β
- N represents the segment size

Equation 3:

![](RackMultipart20201021-4-yfphtk_html_664ec0fad709d644.png)

- ܲP is the normalized power spectral density
- i is an index that cover the entire length of P
- N is the number of samples contained in the segment of the acceleration

**Modelling and statistics**

- Decision trees models were developed to identify activity types
- Activity task were grouped. Categories:
  - &quot;lie&quot;, &quot;sit&quot;, &quot;stand&quot;, &quot;dynamic standing&quot; (DS), &quot;walk&quot;, &quot;run&quot;, and &quot;cycle&quot;.
  - The lying task was labeled as &quot;lie&quot;.
  - the sitting and working on a computer tasks were labeled as &quot;sit&quot;
  - the standing task was labeled as &quot;stand
  - The washing dishes task, dynamic standing, was labeled as &quot;DS&quot;
  - The walking along a corridor, walking downstairs, walking upstairs and walking outdoor tasks were labeled as &quot;walk&quot;.
  - The running and cycling tasks were labeled as &quot;run&quot; and &quot;cycle&quot;, respectively.
- Development of the decision tree consisted of two main steps:
  - The first step was the selection of the best features to use for the classification of the training dataset
  - The second step was the definition of logical conditions based on the selected features to drive the classification of the training dataset.
- For each segment size used to calculate acceleration features, a decision tree was developed
- Classification performance of each decision tree was tested using the leave-one-subject-out cross-validation algorithm
  - classification accuracy and F-score obtained from the cross-validation were used to determine which segment size was the best
- Three separate models were developed to estimate walking, running and cycling speed for the outdoors tasks. Stepwise multiple-linear regression was used to select the best independent elements to include in the models.