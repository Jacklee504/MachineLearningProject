# Reflective changelog

```text
Note.

The reflective changelog was detailed as a requirement in Week 12 notes, which, per Canvas pdf information, were created Monday Nov. 23. I was not made aware of this requirement before this date, and as a result, I had not been keeping a document of this sort. This changelog was created following this requirement being detailed and outlines what decisions I can remember and what I can see in Git history. As a result, it may not contain every decision made throughout the progression of the project.
```

## 16 September - Initial Project Setup
I created the GitHub repository for the machine learning project to track the work carried out throughout the semester. I decided to implement the project using Python scripts rather than a notebook, with separate directories for source code and documentation.

## 29 September - Milestone 1: Dataset Selection and Proposal
I spent time researching suitable datasets for the project. I chose the HELOC dataset as it had a clearly defined target variable, a sufficient number of records and a practical application of classification.

I initially proposed using a dummy classifier, logistic regression, random forest and gradient boosting. I also identified that the dataset contained special codes which would require further investigation during the data audit.

As the licence of the dataset on Kaggle was listed as unknown, I decided to keep the CSV outside of the Git repository and instead provide instructions for obtaining it.

## 15 October - Initial Data Audit and Preprocessing
During the initial data audit, I found that despite there being no NaN values, the dataset contained special codes representing missing or unavailable information. I identified 588 records where every predictor was -9 and decided to remove these as they contained no usable predictor information. I also removed one additional duplicate.

Rather than removing every record containing missing values, I decided to use median imputation and missingness indicators, allowing me to retain records containing other useful predictor information.

I implemented a stratified 80/20 train/test split with a fixed random seed of 42. This allowed me to maintain similar class proportions across both sets and reproduce the results.

## 28 October - Milestone 2: Further Data Audit
I expanded the data audit by examining the descriptive statistics of the predictors after treating the special codes as missing values. I found a number of values which were unusually high in comparison to their 75th percentiles.

For example, the maximum value for MSinceOldestTradeOpen was 803 months, compared with a 75th percentile of 257 months. I decided not to remove these values as there was no evidence that they were incorrect.

This gave me a better understanding of the importance of understanding the dataset before making decisions on what values should be removed.

## 4 November - Baseline Results and Documentation
I improved the documentation of the baseline results and moved them into a separate Markdown file.

The dummy classifier achieved a Bad recall of 1.000 but incorrectly classified every Good case as Bad. It also achieved a ROC-AUC of 0.500. These results gave me a better understanding of why multiple evaluation metrics should be used when evaluating a model, as evaluating Bad recall alone would give a misleading indication of its performance.

## 10 November - Milestone 3: Model Comparison
I implemented logistic regression and random forest to investigate whether the additional complexity of random forest would result in better performance. I used standardisation for logistic regression and retained the same train/test split and evaluation procedure for both models.

The results showed that both models performed considerably better than the dummy baseline, but the difference in performance between the two learned models was relatively small.

I also generated a confusion matrix for random forest and compared the errors made by both models. Random forest correctly identified 18 additional Bad cases but incorrectly classified four additional Good cases as Bad.

At this stage I preferred random forest, but due to the similarity in performance between the models, I decided that further evaluation across different partitions of the training data would be beneficial.

## 23 November - Milestone 4: Cross-Validation and Further Evaluation

Following the results of Milestone 3, I introduced five-fold stratified cross-validation to compare the performance of both learned models across different partitions of the training data. The preprocessing was fitted within each fold to prevent data leakage.

Random forest achieved slightly higher mean Bad recall and Bad F1, while logistic regression achieved higher mean ROC-AUC.

These results led me to reconsider how confident I could be in my preference for random forest. Although I still preferred random forest due to the importance I placed on Bad recall and Bad F1, the results showed that neither model had a clear overall advantage.

## 23 - 26 November - Final Report and Reflection

While completing the final report, I further examined the results and considered their relevance to predicting credit performance. I considered the consequences of false positives and false negatives and how the importance of each type of error could influence model selection.

I also identified limitations of the project, including the lack of external validation, fairness assessment and individual prediction explanations.

If I were to continue working on this project, I would investigate hyperparameter tuning, the effects of changing classification thresholds and the influence of individual predictors on model predictions.

Throughout the project, I gained a better understanding of the importance of data preparation, preventing data leakage and selecting appropriate evaluation metrics, rather than focusing solely on the performance of the models.

## Assistance Declaration

As a result of the announcement of the requirement of this file coming in the days prior to submission, I used ChatGPT Codex solely to trace the Git history of my repository, and to assist me with overviews of the changes of each commit. I then used the change information to add the above entries, none of which were generated with AI.