# Data Statement

FICO HELOC dataset from Kaggle:

https://www.kaggle.com/datasets/averkiyoliabev/home-equity-line-of-creditheloc


FICO xML Challenge:

https://investors.fico.com/news-releases/news-release-details/fico-announces-xml-challenge/

## Intended Use

The dataset is used for an academic comparison of machine learning models for predicting HELOC credit performance. It is not intended for making real-world lending decisions.

## Access

Download the CSV from Kaggle and save it as private/heloc_dataset_v1.csv from the project root. 

The licence on Kaggle is listed as unknown. The CSV is therefore excluded from the repository as redistribution permission has not been confirmed.

## Contents and preparation

The CSV contains 10,459 records and 24 columns. The target, RiskPerformance, contains 5,000 Good and 5,459 Bad labels. The 23 predictors describe credit history, including delinquencies, credit enquiries, and credit utilisation.

The workflow removes 588 records with all predictors set to -9 and one further duplicate, leaving 9,870 records. Remaining values of -7, -8, and -9 are treated as missing. See the [data audit](../docs/data_audit.md) for details.

Missing values are replaced using training-set predictor medians, with missingness indicators added. Standardisation is also used for logistic regression.

## Limitations

The available documentation does not establish the collection period or how representative the records are of other applicant populations. The dataset lacks the demographic fields needed to assess performance across protected groups.
