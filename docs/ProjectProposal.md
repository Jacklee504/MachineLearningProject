# Milestone 1: Project Proposal

## Project title and classification question:

'Can Machine Learning models be used to predict whether a HELOC applicant will have Good or Bad credit performance?' 

## Dataset Name, Source, Licence, Citation

Home Equity Line of Credit (HELOC)

Source: FICO Explainable Machine Learning Challenge

Dataset used: https://www.kaggle.com/datasets/averkiyoliabev/home-equity-line-of-creditheloc

Licence: Kaggle labels Licence as Unknown

Citation: FICO. (2018). Home Equity Line of Credit (HELOC) dataset. Accessed via Kaggle.

## Target variable, main input features

Target variable: 'RiskPerformance' - Good/Bad Classification

23 credit-history features covering credit account history, delinquencies, recent credit inquiries, credit utilisation, account balances and external risk estimates.


## Records and data-quality issues

- 10459 records - 5000 Good, 5459 Bad.
- 23 predictor features
- Contains special coded values -7, -8, and -9 that require preprocessing


## Proposed baseline, candidate models, evaluation metrics

Baseline: Dummy classifier

Models: Logistic Regression, Random Forest, Gradient Boosting

Evaluation Metrics: Accuracy, Precision, Recall, F1-score, ROC-AUC, confusion matrix

## Privacy, fairness, misuse, or other responsible-ML risks

Credit-risk predictions can affect access to financial products, so incorrect classifications and model interpretability are important. The dataset is historical and may not represent all populations or current lending conditions. The models will therefore be treated as an academic prediction exercise rather than a system suitable for real lending decisions.


## Link to online repository
https://github.com/Jacklee504/MachineLearningProject
