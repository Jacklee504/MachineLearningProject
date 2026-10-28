# HELOC Credit Performance Project

This project predicts whether a HELOC applicant has Good or Bad credit performance. See the [proposal](docs/ProjectProposal.md) 
and [data audit](docs/data_audit.md).

## Run

Use Python 3.12 in a virtual environment. Download the [HELOC dataset](https://www.kaggle.com/datasets/averkiyoliabev/home-equity-line-of-creditheloc) 
and place it at private/heloc_dataset_v1.csv before running the script.

From the project directory:

```bash
python -m pip install -r src/requirements.txt
python src/data_audit.py
python src/baseline.py
```

## Baseline results

The code removes 588 rows with all predictors equal to -9 and one other duplicate. It treats -7, -8 and -9 as missing 
values, then uses a stratified 80/20 split and training-only median imputation. The Dummy Classifier predicts Bad for 
every test case.

The split uses random seed 42 and Bad is the positive class (1)

Accuracy: 0.520  
Bad precision: 0.520  
Bad recall: 1.000  
Bad F1: 0.684  
ROC-AUC: 0.500  

Confusion matrix (actual Good/Bad by predicted Good/Bad):<br>[0, 947],<br> [0, 1027]

Repository: [MachineLearningProject](https://github.com/Jacklee504/MachineLearningProject).
