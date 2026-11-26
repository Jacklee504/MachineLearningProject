# Results Tables

## Training-set cross-validation (5 stratified folds):
| Model | Bad F1 (mean ± SD) | Bad recall (mean ± SD) | ROC-AUC (mean ± SD) |
|---|:---:|:---:|:---:|
| LogisticRegression | 0.746 ± 0.009 | 0.753 ± 0.016 | 0.801 ± 0.011 |
| RandomForest | 0.749 ± 0.007 | 0.767 ± 0.011 | 0.792 ± 0.010 |

## Held-out test results:
| Model | Accuracy | Bad precision | Bad recall | Bad F1 | Good recall | ROC-AUC |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Dummy Baseline | 0.520 | 0.520 | 1.000 | 0.684 | 0.000 | 0.500 |
| LogisticRegression | 0.725 | 0.730 | 0.748 | 0.739 | 0.700 | 0.801 |
| RandomForest | 0.732 | 0.732 | 0.765 | 0.748 | 0.696 | 0.802 |

| Model | Good → Good | Good → Bad | Bad → Good | Bad → Bad |
|---|:---:|:---:|:---:|:---:|
| Dummy Baseline | 0 | 947 | 0 | 1027 |
| LogisticRegression | 663 | 284 | 259 | 768 |
| RandomForest | 659 | 288 | 241 | 786 |
