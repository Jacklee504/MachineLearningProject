# Model Comparison

All models use the same 9870 cleaned rows and 80/20 stratified split with random state 42.
The test set contains 947 Good and 1027 Bad cases, and uses Bad as the positive class (1).
Missing values -7, -8, and -9 are imputed using feature medians learned from the training data.


Each model uses default settings, with the exceptions of the dummy model using strategy="prior" and logistic regression using max_iter=1000. No tuning was performed.


## Training-set cross-validation

Logistic regression and random forest were compared using five stratified folds of the training set, shuffled with random state 42. Each pipeline fits its imputation and any scaling within each fold. Values are the mean ± standard deviation across folds; Bad is the positive class.

| Model | Bad F1 | Bad recall | ROC-AUC |
|---|---:|---:|---:|
| LogisticRegression | 0.746 ± 0.009 | 0.753 ± 0.016 | 0.801 ± 0.011 |
| RandomForest | 0.749 ± 0.007 | 0.767 ± 0.011 | 0.792 ± 0.010 |

## Held-out test results

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

Random forest is the current preference for identifying Bad cases. Its mean cross-validation Bad recall is 0.767 versus 0.753 for logistic regression, while mean Bad F1 is close (0.749 versus 0.746). Logistic regression has the higher cross-validation ROC-AUC (0.801 versus 0.792). The held-out results also favour random forest slightly on Bad recall and F1, but one test split and these small differences do not establish that it is consistently better.
