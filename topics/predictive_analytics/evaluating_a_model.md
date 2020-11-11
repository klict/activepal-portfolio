# evaluating a model

## Activity classification
### Cross-validation
In the second and third version we have used cross-validation code to evaluate our dataset. 
I have tried to implement crossvalidation with kfold. The issues I got such high results that it was not trustable. So i used sklearn cross validation.

````python
from sklearn.model_selection import cross_val_score, StratifiedKFold, KFold
import seaborn as sn
from sklearn.model_selection import cross_val_predict

rfc = RandomForestClassifier(n_estimators=287, random_state=0)
pred_y = cross_val_predict(rfc, x, y)

accuracy_scores = cross_val_score(rfc, x, y, scoring='accuracy')
recall_scores = cross_val_score(rfc, x, y , scoring='recall_micro')
precision_scores = cross_val_score(rfc, x, y , scoring='precision_micro')

print("Accuracy: %0.2f (+/- %0.2f)" % (accuracy_scores.mean(), accuracy_scores.std() ))
print("Recall: %0.2f (+/- %0.2f)" % (recall_scores.mean(), recall_scores.std() ))
print("Precision: %0.2f (+/- %0.2f)" % (precision_scores.mean(), precision_scores.std() ))
````
src: [all_steps_activity_recognition_v3_analysis.ipynb](../../evidence/python_notebook/all_steps_activity_recognition_v3_analysis.ipynb)

### Training, validation and test split
The evaluation of activity recongition model was done by looking at validation and test dataset in the final version.
The test dataset includes 3 participants which the model never ever saw.
In this way we get a clear idea that if the model has generalized enhough to get 80% percent of accuracy.

````python
test_users = ['BMR032', 'BMR042', 'BMR098']
````
This function buils dataset and excludes automaticly correspodents from `test_users`. 
````python
def extract_features_from_all_correspondents(exclude_test_correspodent = True):
    
    exclude = ['output', 'throughput', 'Test data','.ipynb_checkpoints', 'BRM015', 'BMR035', 'BMR100', 'BMR051', 'BMR027']
    
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

Accuracy, precision and recall scores of test and validation dataset:

|type dataset|Accuracy|Precision|Recall|
|------------|--------|---------|------|
|Validation|0.92|0.94|0.92|
|Test|0.79|0.87|0.80|

From this we can see clearly that we do lose 10% of accuracy, precision and recall but it does generalize. We can say from these result that the model can predict activity with 79% accuracy.

src: [all_steps_activity_recognition_final_version.ipynb](../../evidence/python_notebook/all_steps_activity_recognition_final_version.ipynb)


