# Baseline Results

```text
Rows used: 9870
Training rows: 7896
Test rows: 1974
              precision    recall  f1-score   support

        Good       0.00      0.00      0.00       947
         Bad       0.52      1.00      0.68      1027

    accuracy                           0.52      1974
   macro avg       0.26      0.50      0.34      1974
weighted avg       0.27      0.52      0.36      1974

ROC-AUC:   0.500
Confusion matrix (rows: actual Good/Bad; columns: predicted Good/Bad):
[[   0  947]
 [   0 1027]]
``` 


The above shows the model predicts Bad for every case, and misses all Good cases.

The ROC-AUC is 0.500.