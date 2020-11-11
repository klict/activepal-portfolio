# visualizing the outcome of a model
## Activity classification
### Confusion matrix
I have created a confusion matrix using heatmap to see what activity it can't predict accurately.

script I used to plot confusion matrix.
````python
import seaborn as sn

#confusion_matrix(valid_y, prediction_y)
cm = confusion_matrix(valid_y.values.argmax(axis=1), prediction_y.argmax(axis=1), normalize='true')

df_cm = pd.DataFrame(cm, index=activities, columns=activities)
df_cm.head()
plt.figure(figsize = (10,7))
sn.heatmap(df_cm, annot=True, cmap='Blues')

plt.title("Validation dataset")
plt.xlabel("predicted label")
plt.ylabel("true label")
````

src: [all_steps_activity_recognition_final_version.ipynb](../../evidence/python_notebook/all_steps_activity_recognition_final_version.ipynb)
