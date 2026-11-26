# Model Card

## Model Overview

Prediction task: Good or Bad HELOC credit performance 
Models: Dummy classifier (baseline), logistic regression, random forest
Framework: Python and scikit-learn

See the [Data Statement](data_statement.md) for information on the dataset, its source and limitations.

## Intended Use

The models are intended for the academic prediction and comparison of HELOC credit performance. They are not intended for making real-world lending decisions.

## Model Configuration

| Model | Configuration |
|---|:---:|
| Dummy classifier | strategy="prior" |
| Logistic regression | max_iter=1000, random_state=42 |
| Random Forest | random_state=42 |

Median imputation and missingness indicators were used for all three models. Standardisation was also used for logistic regression.

All remaining hyperparameters were kept as the default, and no hyperparameter tuning was performed.

## Evaluation

Evaluation Setup:
- Stratified 80/20 Train/Test split with random_seed=42
- 7,896 training records and 1,974 test records
- Five-fold stratified cross-validation on the training data for both learned models
- Bad treated as the positive class
- Preprocessing fitted on training data only

Results can be seen in the [Model Comparison](model_comparison.md).

## Error Analysis

False positives represent Good cases incorrectly classified as Bad, while false negatives represent Bad cases incorrectly classified as Good.

| Model | False Positives (FP) | False Negatives (FN) |
|---|:---:|:---:|
| Dummy Classifier | 947 | 0 |
| Logistic Regression | 284 | 259 |
| Random Forest | 288 | 241 |

Compared with logistic regression, random forest had 18 fewer false negatives but four additional false positives. This shows that random forest is slightly better at identifying Bad cases, at the expense of incorrectly classifying more Good cases.

The [Random Forest Confusion Matrix](random_forest_confusion_matrix.png) provides a visual representation of its classification results.

## Limitations

- No hyperparameter tuning
- No evaluation on external datasets
- No fairness assessment across protected groups
- No analysis of individual prediction explanations
- Unknown financial costs associated with false positives and false negatives

## Conclusion

Random forest is my preferred model as it achieved slightly higher Bad recall and Bad F1 than logistic regression. However, logistic regression achieved a higher mean ROC-AUC during cross-validation. Due to the small differences in performance, further evaluation would be required to determine whether either model consistently performs better than the other.
