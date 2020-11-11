# configuring a model
## Activity recognition model
After we decided that we were going with Random Forest model to classify our data we looked at parameters.
Which parameters was need to configure was based on experiments and documentation on [sklearn](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).

Just setting 2 parameter we already got some great results

## Random state
We found out that results of the model changes each run. To remedy this we have decided to set random state to 0

## Amount of Trees
In the first version of our model I have chosen a random number of trees which was 20. 
It gave pretty good results but we wanted to see if there were another number that even gave better result.
For this i created a script that visualises the results and automaticlly provides right number of trees.

````python
#### Quick analysis
accuracy_scores = []
f1_scores = []
#precision_scores = []

n_estimator_numbers = range(1,300)

for i in n_estimator_numbers:
    rfc_t = RandomForestClassifier(n_estimators=i, random_state=0)
    rfc_t.fit(train_x, train_y)
    
    predictions = rfc_t.predict(valid_x)
    
    accuracy_scores.append(accuracy_score(valid_y, predictions, normalize=True))
    f1_scores.append(f1_score(valid_y, predictions, average='micro' ))
    #precision_scores.append(precision_score(valid_y, predictions, average='micro'))

````

````python
plt.plot(n_estimator_numbers, accuracy_scores, label='accuracy')
plt.plot(n_estimator_numbers, f1_scores, label='f1')

plt.xlabel('Trees')
plt.ylabel('score')
#plt.plot(n_estimator_numbers, precision_scores, label='precision')

plt.legend()
````

````python
np_accuracy_scores = np.array(accuracy_scores)
np_f1_scores = np.array(f1_scores)

best_accuracy_index = np.argmax(np_accuracy_scores)
best_f1_index = np.argmax(np_f1_scores)

print('accuracy: ', n_estimator_numbers[best_accuracy_index])
print('f1: ', n_estimator_numbers[best_f1_index])
````
Best amount of trees i got was `287`.

src: [all_steps_activity_recognition_v3_analysis.ipynb](../../evidence/python_notebook/all_steps_activity_recognition_v3_analysis.ipynb)

## Intensity Classification

src: [intensity_classification.ipynb](../../evidence/python_notebookintensity_classification.ipynb)

