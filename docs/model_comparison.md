# Model Comparison

All models use the same 9870 cleaned rows and 80/20 stratified split with random state 42.
The test set contains 947 Good and 1027 Bad cases, and uses Bad as the positive class (1).
Missing values -7, -8, and -9 are imputed using feature medians learned from the training data.


Each model uses default settings, with the exceptions of the dummy model using strategy="prior" and logistic regression using max_iter=1000. No tuning was performed.


| Model | Accuracy | Bad precision | Bad recall | Bad F1 | Good recall | ROC-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Dummy Baseline | 0.520 | 0.520 | 1.000 | 0.684 | 0.000 | 0.500 |
| LogisticRegression | 0.725 | 0.730 | 0.748 | 0.739 | 0.700 | 0.801 |
| RandomForest | 0.732 | 0.732 | 0.765 | 0.748 | 0.696 | 0.802 |

| Model | Good → Good | Good → Bad | Bad → Good | Bad → Bad |
|---|---:|---:|---:|---:|
| Dummy Baseline | 0 | 947 | 0 | 1027 |
| LogisticRegression | 663 | 284 | 259 | 768 |
| RandomForest | 659 | 288 | 241 | 786 |

## Analysis

The dummy model predicts every case as Bad and has 0.500 ROC-AUC.

Both learned models are capable of identifying both classes. 

Comparing Logistic Regression (LR) with Random Forest (RF), RF has 18 fewer Bad cases as Good (241 versus 259), but it labels 4 more Good cases as Bad (288 versus 284).


## Conclusion

Random forest is preferred to Logistic Regression as it has higher Bad F1 (0.748, greater by 0.009) and Bad recall (0.765, greater by 0.017), and has a ROC-AUC greater by 0.0003. 

Because of the similarity between RF and LR, the two models should be compared further across training-data folds.