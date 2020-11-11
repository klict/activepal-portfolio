# selecting a model
## Activity classification 
The model i selected for activity recognition was based on literature research and experiments.
Chapter of the paper [detection of type, duration and intensity of physical activity using an accelerometer](../../evidence/documents/physical_activity_recognition.pdf) convinced me to use decision tree model.
The result we got from it were quit good but it was prone to over-fitting and I wanted to try other models. The next model I tried was Random forest model.
The reason for it because the experiment gave much better result and articles I read explained how it worked and what advantages it brought with. For example it was less prone to be biased than disicion tree because of it working.

We looked at accuracy, precision and recall and concluded that Random forest would be better model to work further with.

|Model | Accuracy | Precision | Recall |
|-------|----------|-----------|--------|
|Decision tree |0.96|0.96|0.96|
|Random forest |0.97|0.98|0.98|

Evidence: [all_steps_activity_recognition.ipyn](../../evidence/python_notebook/all_steps_activity_recognition.ipynb)

These results are great of course but this causes by balancing dataset. 
At the time we didn't know this nor did we feel weird about it. 
In the second version  we have disabled the script balances dataset to give more realistic result.




